<!--
SYNC IMPACT REPORT
==================
Version: 0.0.0 → 1.0.0 (INITIAL CONSTITUTION)
Rationale: Initial constitution establishment for PMF-Kit project

Added Sections:
- Complete constitution framework for PMF-Kit
- 7 core principles adapted for product-market-fit discovery
- Naming convention strategy to avoid conflicts with other *-kit variants
- Governance and versioning framework

Templates Requiring Updates:
- ⚠ /templates/plan-template.md - Needs PMF-specific constitution check gates
- ⚠ /templates/spec-template.md - Needs PMF-specific user story guidelines
- ⚠ /templates/tasks-template.md - Needs PMF-specific task categories
- ⚠ /.claude/commands/*.md - Need Keep old commands, this is the working commands for current spec-kit for coding agents
- ⚠ CLI implementation - Needs "pmf" command instead of "specify"

Follow-up TODOs:
- Update all command files to use pmfkit.* prefix
- Update CLI implementation to use "pmf" command name
- Create kit-namespace.md documentation for variant creators
- Add PMF-specific metrics and validation criteria to templates
- Develop comprehensive /refs/ documentation for PMF methodology
-->

# PMF-Kit Constitution

## Preamble

PMF-Kit is a specialized variant of [spec-kit](https://github.com/github/spec-kit)
designed for product-market-fit discovery and validation of AI SaaS products. This
constitution adapts the spec-driven development methodology from software engineering
to the domain of product management, market research, and iterative customer validation.

**Purpose**: Enable structured, AI-agent-assisted workflows for finding and validating
product-market-fit through systematic specification, planning, and execution of PMF
discovery experiments and initiatives.

**Scope**: This kit demonstrates how spec-driven methodologies can extend beyond coding
to other complex knowledge work including project management, product design, marketing,
and business writing.

## Core Principles

### I. Specification-First Approach

**Principle**: Every PMF discovery initiative MUST begin with a clear, testable
specification of what we're trying to learn, who we're learning from, and how we'll
measure success.

**Requirements**:
- Define hypotheses before running experiments
- Specify success criteria before collecting data
- Document assumptions explicitly in spec.md
- Use structured templates to ensure completeness
- Prioritize learning objectives (P1, P2, P3...)

**Rationale**: Without clear specifications, PMF discovery becomes reactive "vibe-based"
product development. Structured specs enable systematic hypothesis testing and prevent
confirmation bias.

### II. Customer-Evidence-Driven

**Principle**: All PMF claims MUST be supported by direct customer evidence—not opinions,
assumptions, or proxy metrics.

**Requirements**:
- User stories MUST reference real customer conversations or data
- Requirements MUST be traceable to customer pain points
- Success criteria MUST include measurable customer behavior
- Plans MUST specify evidence collection methods
- Tasks MUST include customer validation checkpoints

**Rationale**: PMF is achieved when customers pull your product from you, not when you
push it to them. This requires evidence of genuine customer need and willingness to pay.

### III. Iterative Validation

**Principle**: PMF discovery MUST follow build-measure-learn cycles with independent,
testable increments.

**Requirements**:
- User stories MUST be independently testable
- Each story MUST deliver standalone learning value
- Experiments MUST have clear success/failure criteria
- Implementation MUST allow early termination if hypothesis fails
- Checkpoints MUST validate learning before proceeding

**Rationale**: PMF discovery is inherently uncertain. Independent validation points enable
fast pivots and prevent sunk cost fallacy.

### IV. Minimal Viable Process

**Principle**: Use the simplest process that achieves the learning objective. Complexity
MUST be explicitly justified.

**Requirements**:
- Default to qualitative before quantitative research
- Start with manual processes before automation
- Use smallest viable sample sizes
- Prefer direct customer contact over surveys
- Document why more complex methods are necessary

**Rationale**: Over-engineered research processes slow learning velocity. Simple approaches
often yield richer insights faster.

### V. Cross-Functional Integration

**Principle**: PMF discovery MUST integrate insights across product, engineering, sales,
marketing, and customer success.

**Requirements**:
- Specs MUST consider technical feasibility (via /pmfkit.plan)
- Plans MUST address go-to-market implications
- Tasks MUST include cross-functional validation
- Research MUST capture diverse stakeholder perspectives
- Documentation MUST be accessible to non-technical stakeholders

**Rationale**: PMF exists at the intersection of customer desirability, technical
feasibility, and business viability. Siloed discovery leads to solutions that fail
in market.

### VI. Kit Namespace Isolation

**Principle**: PMF-Kit MUST coexist with other *-kit variants without naming conflicts.

**Requirements**:
- CLI command MUST be `pmf` (not `specify`)
- Package name MUST be `pmf-cli` (not `specify-cli`)
- Slash commands MUST use `pmfkit.*` prefix (not `pmfkit.*`)
- Templates MUST reference correct command namespaces
- Documentation MUST explain multi-kit installation strategy

**Rationale**: Users may install multiple kit variants (pmf-kit, pd-kit, marketing-kit)
on the same system. Unique namespaces prevent conflicts and enable specialized workflows
to coexist.

**Implementation**:
```bash
# CLI commands
pmf init <project>              # NOT: specify init
pmf check                       # NOT: specify check

# Agent commands
/pmfkit.constitution           # NOT: /pmfkit.constitution
/pmfkit.specify                # NOT: /pmfkit.specify
/pmfkit.plan                   # NOT: /pmfkit.plan
/pmfkit.tasks                  # NOT: /pmfkit.tasks
/pmfkit.implement              # NOT: /pmfkit.implement
/pmfkit.clarify                # NOT: /pmfkit.clarify
/pmfkit.analyze                # NOT: /pmfkit.analyze
/pmfkit.checklist              # NOT: /pmfkit.checklist
```

### VII. Template Extensibility

**Principle**: PMF-Kit serves as a reference implementation for creating domain-specific
kit variants.

**Requirements**:
- Templates MUST be adaptable to other domains
- Documentation MUST explain adaptation process
- /refs/ directory MUST contain comprehensive guides
- Examples MUST show prompt patterns for customization
- Architecture MUST support pluggable workflows

**Rationale**: Spec-driven development applies broadly beyond software. PMF-Kit demonstrates
the pattern for creating specialized variants (pm-kit, pd-kit, marketing-kit,
biz-writing-kit).

## PMF-Specific Quality Standards

### Research Quality

- Interview notes MUST be timestamped and attributed
- Quotes MUST be verbatim (not paraphrased)
- Sample sizes MUST be documented
- Selection bias MUST be acknowledged
- Contradictory evidence MUST be included

### Hypothesis Quality

- Hypotheses MUST be falsifiable
- Hypotheses MUST specify validation criteria
- Hypotheses MUST identify riskiest assumptions
- Null hypotheses MUST be documented
- Alternative explanations MUST be considered

### Evidence Quality

- Primary sources preferred over secondary
- Behavioral evidence preferred over stated preferences
- Paying customers weighted more than free users
- Recent evidence weighted more than historical
- Consistent patterns across segments required

## Development Workflow

### Phase 0: Constitution (Required)

Use `/pmfkit.constitution` to establish project-specific principles beyond this base
constitution. Examples:
- Target market definitions
- PMF metrics and thresholds
- Research methodologies approved
- Compliance and privacy requirements
- Decision-making frameworks

### Phase 1: Specification (/pmfkit.specify)

Define WHAT you're trying to learn and WHY. Focus on:
- Learning objectives (not features)
- Target customer segments
- Hypotheses to test
- Success criteria
- Edge cases and risks

Do NOT specify technical implementation at this phase.

### Phase 2: Clarification (/pmfkit.clarify)

Before planning, run structured clarification to identify gaps:
- Ambiguous customer definitions
- Unclear success metrics
- Missing validation criteria
- Underspecified hypotheses
- Unstated assumptions

### Phase 3: Planning (/pmfkit.plan)

Define HOW you'll execute discovery. Specify:
- Research methods (interviews, surveys, experiments)
- Sample sizes and selection criteria
- Tools and platforms
- Data collection instruments
- Analysis approach

### Phase 4: Task Breakdown (/pmfkit.tasks)

Generate actionable, dependency-ordered tasks:
- Recruit participants
- Conduct research
- Analyze results
- Validate findings
- Document learnings

Tasks MUST be grouped by learning objective with independent validation checkpoints.

### Phase 5: Execution (/pmfkit.implement)

Execute tasks systematically:
- Follow TDD equivalent: Hypothesis → Data collection → Analysis
- Validate at each checkpoint
- Document evidence continuously
- Update specs based on learnings
- Decide continue/pivot/kill based on criteria

## Governance

### Amendment Procedure

1. Propose changes via pull request to `/memory/constitution.md`
2. Document rationale and impact in Sync Impact Report
3. Update version following semantic versioning
4. Validate all templates for consistency
5. Update dependent documentation
6. Require sign-off from project maintainers

### Versioning Policy

- **MAJOR (X.0.0)**: Principle removal, incompatible governance changes
- **MINOR (0.X.0)**: New principles, expanded sections, new workflows
- **PATCH (0.0.X)**: Clarifications, typo fixes, non-semantic changes

### Compliance Review

- All specs MUST reference constitution principles
- All plans MUST pass Constitution Check gates
- All PRs MUST verify compliance
- Non-compliance MUST be explicitly justified in Complexity Tracking
- AI agents MUST validate against constitution before generation

### Constitution Inheritance

PMF-Kit inherits architectural patterns from spec-kit but adapts content for PMF domain:

**Inherited**:
- CLI installation and management
- Template-based workflow structure
- Multi-agent support architecture
- Branch-per-feature organization
- Semantic versioning approach

**Adapted**:
- Principle definitions (PMF vs. software engineering)
- Success criteria (customer evidence vs. code quality)
- Task categories (research vs. development)
- Validation checkpoints (learning vs. testing)

### Living Document

This constitution MUST evolve as PMF-Kit matures:
- Incorporate learnings from real PMF discovery projects
- Refine principles based on user feedback
- Add domain-specific patterns as they emerge
- Maintain consistency with upstream spec-kit innovations
- Balance standardization with flexibility

**Version**: 1.0.0 | **Ratified**: 2025-12-03 | **Last Amended**: 2025-12-03
