# PMF Specification: Workflow Optimization Command

**Feature Branch**: `003-workflow-optimization`
**Created**: 2025-12-04
**Status**: Draft
**Discovery Focus**: AI Agent Workflow Optimization Infrastructure

## Overview

**What we believe**: PMF discovery requires iterative refinement - specs, plans, and workflows must be continuously evaluated and improved based on real-world feedback and measurable outcomes.

**Who we're solving for**: Product teams, PMF researchers, and AI practitioners using PMF-Kit who need systematic approaches to improve their discovery workflows, research quality, and agent outputs beyond manual iteration.

**Why now**: As AI agents become central to PMF discovery workflows (v0.0.2-0.0.3), teams need automated optimization to scale quality improvements without manual prompt engineering bottlenecks. State-of-the-art agent evaluation frameworks (LLM-as-Judge, MIPROv2, TextGrad) now make systematic optimization feasible.

---

## Personas & Segments *(mandatory)*

### Primary Persona: PMF Product Manager

**Context**:
- **Role**: Product Manager leading PMF discovery for AI SaaS startup
- **Company**: Seed to Series A startup (5-20 person team), AI/LLM product
- **Team**: Works with founders, engineers, growth/marketing, and customer success
- **Tools they use**: PMF-Kit, Claude Code/GitHub Copilot, Notion/Linear, customer interview tools
- **Success metric**: Validated PMF hypotheses leading to measurable product improvements and customer adoption

**Pain Profile**:
- **Top pain**: Iterating on PMF research workflows is manual and time-consuming - unclear if spec quality, research methods, or task execution needs improvement (frequency: every sprint)
- **Current workaround**: Ad-hoc refinement based on intuition; manually reviewing outputs and rewriting prompts/specs without systematic measurement
- **Willingness to try**: Actively seeking structured approaches to improve research quality and reduce discovery cycle time

### Secondary Persona: AI Product Researcher

**Context**:
- **Role**: Research lead or principal researcher focused on product-market fit
- **Company**: Series A-B company with established product, exploring new markets/segments
- **Team**: Collaborates with data analysts, user researchers, product managers
- **Tools they use**: PMF-Kit workflows, analytics platforms, research repositories
- **Success metric**: High-confidence insights that directly inform product decisions and market positioning

**Pain Profile**:
- **Top pain**: Research outputs vary in quality; difficult to know if workflow, agent instructions, or research design needs adjustment (frequency: ongoing)
- **Current workaround**: Manual review cycles with team feedback; inconsistent quality standards across researchers
- **Willingness to try**: Looking for evidence-based methods to validate and improve research methodology

### Segment You're NOT Building For

**Enterprise IT teams** focused on operational workflows (not PMF discovery), and **individual hobbyists** without structured PMF processes. This command requires existing PMF-Kit usage patterns and understanding of spec-driven development.

---

## Problems & Jobs-to-Be-Done (JTBD) *(mandatory)*

### Primary JTBD #1: Evaluate Workflow Quality (Priority: P1)

**Job Story**: When I complete a PMF discovery workflow (spec, plan, tasks), I want to systematically evaluate output quality across multiple dimensions, so I can identify specific improvement areas with confidence rather than relying on subjective judgment.

**Current Workaround**: Manual review with team discussion; inconsistent evaluation criteria; reliance on individual expertise and "gut feel"

**Frequency**: After every major workflow execution (weekly to bi-weekly during active discovery)

**Evidence of willingness-to-pay**: Teams currently hire external consultants or dedicate senior staff time for quality reviews - indicating willingness to invest in systematic evaluation

**Success signal**: Clear, quantified scores across evaluation dimensions (e.g., "Spec completeness: 7/10, JTBD clarity: 8/10") with specific evidence for each rating

### Primary JTBD #2: Generate Actionable Improvement Suggestions (Priority: P1)

**Job Story**: When workflow evaluation reveals quality gaps, I want specific, ranked suggestions for improvement, so I can prioritize high-impact changes without researching optimization techniques myself.

**Current Workaround**: Brainstorming sessions; consulting documentation; trial-and-error refinement; asking experienced practitioners for advice

**Frequency**: After evaluation of each workflow (tied to JTBD #1 frequency)

**Evidence of willingness-to-pay**: Teams spend significant time in retrospectives and improvement planning meetings - automation would recover this time

**Success signal**: Receive 5-7 concrete suggestions ranked by impact, with clear before/after examples showing what to change

### Primary JTBD #3: Automatically Apply Improvements (Priority: P2)

**Job Story**: When I have improvement suggestions, I want automated application of changes to specs/plans/workflows, so I can quickly test refined versions without manual rewriting.

**Current Workaround**: Manually editing spec files, rewriting prompts, updating templates - time-intensive and error-prone

**Frequency**: During improvement cycles (1-2 times per workflow iteration)

**Evidence of willingness-to-pay**: Teams using AI assistants for rewriting already demonstrate willingness to delegate refinement tasks to automation

**Success signal**: Updated spec/plan/workflow artifacts that incorporate suggestions, with tracked changes showing what was modified

---

## Hero Workflows *(mandatory)*

### Hero Workflow: Optimize Existing Specification

**Why this workflow matters**: Connects directly to JTBD #1, #2, and #3 - takes an existing spec.md through full evaluation-suggestion-improvement cycle

**End-to-end flow**:

1. **Input**: Completed spec.md file (from previous `/pmfkit.specify` run), optional evaluation criteria customization
2. **Process**:
   - User runs `/pmfkit.optimize spec` on target spec file
   - System evaluates spec across 8-10 quality dimensions (persona clarity, JTBD specificity, success metrics, etc.)
   - System generates ranked suggestions based on evaluation gaps
   - System applies top suggestions to create improved spec version
   - (Optional) System validates improvements with before/after comparison
3. **Output**:
   - Evaluation report with dimensional scores and evidence
   - Ranked improvement suggestions with rationale
   - Updated spec.md file with tracked changes
   - Validation report showing improvement delta
4. **Success signal**: "This optimization increased spec completeness from 6.5/10 to 8.5/10 in 5 minutes - previously took 2 hours of manual review"

**TTFW (Time-to-First-Workflow) Target**: < 10 minutes from running command to receiving actionable evaluation results

**Guardrails & Error Recovery**:
- What breaks the workflow? Invalid spec format, missing required sections, no baseline to compare against
- How do users recover? Command provides diagnostic errors pointing to specific issues; can run evaluation-only mode first
- What's the backstop if AI fails? Manual review option; command saves original file before modifications; all changes are tracked and reversible

### Hero Workflow 2: Iterative Optimization Loop

**Why this workflow matters**: Supports continuous improvement through repeated evaluation-suggestion-improvement cycles (JTBD #3 extended)

**End-to-end flow**:

1. **Input**: Initial workflow artifact (spec, plan, or task list), target quality threshold, maximum iteration count
2. **Process**:
   - Run initial evaluation to establish baseline
   - Loop: Evaluate → Suggest → Improve → Validate
   - Continue until quality threshold met or max iterations reached
   - Track quality trajectory across iterations
3. **Output**:
   - Final optimized artifact
   - Optimization trajectory report (quality scores per iteration)
   - Summary of all applied improvements
4. **Success signal**: "Workflow reached 8.5/10 quality target in 3 iterations (15 minutes total) - would have taken multiple days of manual iteration"

**TTFW Target**: < 20 minutes for 3-iteration optimization loop

**Guardrails & Error Recovery**:
- What breaks the workflow? Quality degradation between iterations, infinite loop conditions, conflicting suggestions
- How do users recover? Circuit breaker stops after quality drops; max iteration limit; user can abort and review intermediate results
- What's the backstop? Each iteration saves incremental versions; full rollback capability to any previous iteration

---

## Success Metrics & PMF Signals *(mandatory)*

### Activation Metrics

- **% of PMF-Kit users who run `/pmfkit.optimize` within first 3 workflows** - Target: 40%+ (indicates perceived value early)
- **% of optimize runs that complete successfully on first attempt** - Target: 85%+ (indicates good UX and error handling)

### Engagement Metrics

- **Average optimizations per active user per month** - Target: 4-6 (1-2 per major workflow artifact)
- **% of users who use iterative mode (>1 iteration)** - Target: 30%+ (indicates understanding of continuous improvement)

### Retention Metrics

- **D7 retention of users who tried optimize** - Target: 60%+ (higher than base PMF-Kit retention)
- **% of users who make optimize part of regular workflow** - Target: 45%+ after 30 days

### AI-Specific Metrics

- **Quality improvement delta (before/after optimization)** - Target: Average +15-25% improvement across evaluation dimensions
- **% of suggested improvements accepted/applied by users** - Target: 70%+ (indicates suggestions are valuable)
- **User-reported quality of evaluation feedback (1-5 scale)** - Target: 4.2+ average

### Business Metrics

- **Time savings per optimization cycle** - Target: 60-80% reduction vs. manual review (2 hours → 20-30 minutes)
- **% of premium users using optimize regularly** - Target: 70%+ (feature drives upgrade value)
- **NPS among optimize users vs. non-users** - Target: +15 point delta

### PMF Validation Threshold

- **User testimonials**: "I can't do PMF discovery without optimize anymore" - from 30%+ of active users
- **Retention lift**: Optimize users show 2x better D30 retention than non-users
- **Quality validation**: External review confirms 80%+ of suggested improvements are valid and high-impact

---

## Constraints & Risks *(mandatory)*

### Technical Feasibility

- **AI evaluation accuracy must be >= 80%** for users to trust automated scoring (validated through comparison with expert human reviews)
- **Latency requirement: < 30 seconds for evaluation phase**, < 60 seconds for full optimize cycle (to maintain flow state)
- **Multi-judge consensus required** to reduce single-LLM bias (3-5 judge models per evaluation)
- **Version compatibility**: Must work with all existing PMF-Kit v0.0.2+ workflow artifacts without breaking changes

### Competitive Landscape

- **Direct competitors**: DSPy optimizers (BootstrapFewShot, MIPROv2), TextGrad, OPRO, PromptBreeder - but these are generic prompt optimization frameworks, not PMF-specific
- **Why we're different**:
  - Domain-specific optimization for PMF discovery (not generic prompting)
  - Integrated into existing PMF-Kit workflow (not separate tool)
  - Non-technical interface for product teams (not ML engineer-focused)
- **Incumbent workaround**: Manual review cycles, ad-hoc refinement, consultant reviews - expensive and slow

### Top 3 PMF Risks & Mitigations

| Risk                                                                             | Impact | Mitigation                                                                                                                                |
|---------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------|
| AI evaluation quality insufficient - users don't trust automated scores         | High   | Validate with 20+ expert reviews comparing automated vs. human scores; target 80%+ agreement; show evidence for each score              |
| Suggestions are too generic/not actionable - users ignore recommendations       | High   | Use multi-aspect analysis (8-10 dimensions); provide specific before/after examples; rank by impact with rationale                      |
| Integration complexity - users struggle to adopt into existing workflows        | Medium | Design as natural extension of existing commands; provide evaluation-only mode for low-commitment trial; comprehensive examples         |

---

## Distribution & Adoption Hypotheses *(mandatory)*

### Primary Channel Hypothesis

- **Channel**: In-product discovery for existing PMF-Kit users (command appears in natural workflow progression)
- **Rationale**: Users who complete `/pmfkit.specify` → `/pmfkit.plan` → `/pmfkit.tasks` are already invested in spec-driven discovery; optimize is logical next step
- **Success criterion**: 40%+ of users who complete 2+ workflows try optimize within 30 days

### Secondary Channels (Ordered by Priority)

1. **Documentation & tutorials**: "How to improve your specs with /pmfkit.optimize" guide featured in README and docs site
2. **Community showcase**: Twitter/X threads showing before/after optimization results with quality improvements
3. **Integration prompts**: CLI suggests "Try /pmfkit.optimize to improve this spec" after workflow completion

### Viral/Network Hypothesis

- **Does collaboration/sharing drive value?** Yes - teams benefit from shared optimization standards and consistent quality
- **If yes**: Teams share optimized spec templates and evaluation criteria configurations; "best practices" emerge from high-performing teams and get adopted broadly

### Early Adopter Profile

- **Who jumps at this first?** PMF practitioners already using PMF-Kit regularly (v0.0.2-0.0.3 users); teams frustrated with inconsistent spec quality
- **Where to find them?** Existing PMF-Kit GitHub discussions, PMF-focused communities (r/SaaS, Indie Hackers), AI product Twitter
- **How to activate them?** Direct outreach to active GitHub users; featured example in release notes; "optimize your existing specs" migration guide

---

## Success Criteria for Discovery Phase *(mandatory)*

Before proceeding to research planning, we consider discovery successful when:

- [x] **Persona Validation**: Product managers and researchers using PMF-Kit confirm pain of manual optimization and willingness to try automated approach
- [x] **JTBD Clarity**: Evaluation, suggestion, improvement jobs consistently mentioned; evidence of time/cost savings motivating automation
- [x] **Hero Workflow Buy-In**: 5+ existing PMF-Kit users validate that optimize workflow addresses real pain in their discovery process
- [x] **Metrics Feasibility**: Evaluation scores, quality deltas, and time savings are measurable with existing PMF-Kit instrumentation
- [x] **Risk Acknowledgment**: AI evaluation accuracy is primary risk; mitigation plan includes multi-judge consensus and human validation baseline
- [x] **Go-to-Market Confidence**: In-product adoption via existing user base is testable immediately with v0.0.4 release

---

## Open Questions

- Should optimize work on plans and tasks in addition to specs, or start spec-only for MVP?
- What is the minimum acceptable quality improvement delta that users would find valuable? (15%? 20%? 25%?)
- Should validation stage be required or optional? (Trade-off: thoroughness vs. speed)

---

## AI Product References

**Products with similar hero workflows** (for pattern reference):
- **DSPy/MIPROv2**: Automated prompt optimization through evaluation-improvement loops → ML practitioners → research/framework adoption
- **TextGrad**: Gradient-based prompt optimization → researchers/developers → paper citations and GitHub stars
- **GitHub Copilot Labs**: Code quality checks and suggestions → developers → feature discovery through IDE integration

**Key PMF patterns we're following**:
- **Progressive enhancement**: Optimize builds on existing workflows users already trust (spec-kit/PMF-Kit foundation)
- **Low-friction trial**: Evaluation-only mode lets users test without commitment to applying changes
- **Measurable value**: Quality scores and time savings provide concrete proof of value (not subjective improvement)

---

## Next Steps

**Immediate**: Run `/pmfkit.clarify` to resolve open questions about scope (spec-only vs. multi-artifact) and quality thresholds

**If clarification passes**: Run `/pmfkit.plan` to design:
- Evaluation framework architecture (multi-judge consensus, rubric dimensions)
- Suggestion generation methodology (root cause analysis, impact ranking)
- Improvement application strategy (TextGrad, MIPROv2, or hybrid approach)

**If risks are high**: Validate AI evaluation accuracy with 10-15 expert reviews before building full optimization pipeline
