<!--
SYNC IMPACT REPORT
==================
Version: 1.0.0 → 2.0.0
Rationale: Complete rewrite for agentii-kit website - a marketplace/gallery platform for Job Kits across professional domains

Modified Sections:
- Complete rewrite from generic PMF-Kit to agentii-kit website specific constitution
- Project name: PMF-Kit → agentii-kit website
- Domain: Generic PMF discovery → Job Kit marketplace/community platform
- All principles adapted for two-sided marketplace discovery and validation

Added Sections:
- Two-sided marketplace principles (kit creators + kit users)
- Community-driven discovery and validation
- Platform network effects and growth loops
- Content quality standards for kit submissions
- Technical architecture principles for scalable gallery platform

Removed Sections:
- Generic PMF research methodology (replaced with marketplace-specific validation)

Templates Requiring Updates:
✅ .specify/templates/plan-template.md - Reviewed for marketplace PMF workflow
✅ .specify/templates/spec-template.md - Reviewed for marketplace user stories
✅ .specify/templates/tasks-template.md - Reviewed for marketplace task categories
✅ .specify/templates/checklist-template.md - Reviewed for marketplace quality gates
⚠️  .specify/templates/agent-file-template.md - May need marketplace-specific guidance

Follow-up TODOs:
- Create detailed personas document for kit creators vs. kit users
- Define marketplace metrics dashboard requirements
- Establish kit quality rubric and submission guidelines
- Map competitive analysis to feature differentiation strategy
- Define technical SEO requirements for kit discoverability
-->

# agentii-kit Website Constitution

## Preamble

**agentii-kit** is a marketplace and community platform for discovering, sharing, and using "Job Kits" - structured, AI-agent-ready workflow templates that extend spec-driven development beyond software engineering to any professional domain (Product Management, Marketing, Legal, Education, etc.).

**Purpose**: Enable product-market-fit discovery and validation for a two-sided marketplace that connects:
1. **Kit Creators** - domain experts who encode their best practices into reusable templates
2. **Kit Users** - professionals seeking structured AI workflows for their domain

**Scope**: This constitution guides PMF discovery for the agentii-kit website platform itself, including marketplace dynamics, community growth, content quality, and platform economics.

**Parent Framework**: This project inherits from PMF-Kit (spec-kit variant) but applies PMF methodology to validate the marketplace concept itself.

## Core Principles

### I. Two-Sided Marketplace Validation

**Principle**: PMF exists only when BOTH kit creators and kit users find sufficient value to participate actively and recommend the platform to peers.

**Requirements**:
- User stories MUST address both creator and user personas explicitly
- Success metrics MUST track supply-side (kit submissions) AND demand-side (kit usage) health
- Research MUST validate value propositions for BOTH sides independently
- Hypotheses MUST test cross-side network effects (more kits → more users → more kits)
- Experiments MUST measure engagement, retention, AND referral rates for both cohorts

**Rationale**: Marketplaces fail when they over-optimize for one side. agentii-kit must achieve balanced growth where kit quality attracts users, and user demand incentivizes creators.

**Critical Metrics**:
- Creator activation rate: % of visitors who submit a kit
- User activation rate: % of visitors who fork/use a kit
- Creator retention: % of creators who submit multiple kits
- Network effects: correlation between kit count and user growth
- Cross-side conversion: % of users who become creators (and vice versa)

### II. Community-First Discovery

**Principle**: PMF validation MUST prioritize direct community feedback over vanity metrics and proxy signals.

**Requirements**:
- Research MUST include qualitative interviews with real kit creators and users
- User stories MUST be traceable to verbatim quotes from community conversations
- Success criteria MUST include qualitative satisfaction scores, not just quantitative usage
- Plans MUST specify community feedback loops (forums, Discord, office hours)
- Tasks MUST include community engagement checkpoints before scaling

**Rationale**: GitHub succeeded because it built for actual developer needs discovered through community interaction. agentii-kit must follow the same community-driven approach.

**Evidence Sources**:
- Creator interviews: "Why did you/would you create a kit?"
- User interviews: "What problem were you trying to solve when you found agentii-kit?"
- Support conversations: Patterns in questions, confusion, feature requests
- Usage analytics: Behavioral data (what do people actually do vs. what they say)

### III. Content Quality Over Quantity

**Principle**: Platform value derives from kit quality, not kit count. A curated library of 20 excellent kits beats 200 mediocre ones.

**Requirements**:
- Specs MUST define explicit quality standards for kit submissions
- Plans MUST include curation mechanisms (review, rating, featured status)
- Tasks MUST implement quality gates before public kit visibility
- Research MUST validate that users prefer fewer high-quality options
- Hypotheses MUST test whether strict quality standards increase or decrease creator participation

**Rationale**: Marketplace quality death spirals occur when low-quality supply drives away demand, which further reduces supply quality. Early curation establishes quality norms.

**Quality Dimensions**:
- **Completeness**: All required template files present and filled
- **Clarity**: Clear documentation, examples, and usage instructions
- **Tested**: Creator has used the kit in real work (not hypothetical)
- **Differentiated**: Solves a problem not addressed by existing kits
- **Maintained**: Creator responds to issues and updates kit over time

### IV. GitHub-Native Distribution

**Principle**: agentii-kit is a discovery layer OVER GitHub, not a replacement. Kits live in Git repositories, and the platform indexes and presents them.

**Requirements**:
- Specs MUST treat GitHub as the source of truth for kit content
- Plans MUST leverage GitHub features (stars, forks, issues, PRs) for social proof
- Tasks MUST implement GitHub OAuth for seamless creator onboarding
- Research MUST validate that target users are comfortable with Git workflows
- Architecture MUST support eventual decentralization (any GitHub repo can be a kit)

**Rationale**: Spec-kit succeeded because it works WITH developer tools, not against them. agentii-kit inherits this "augment, don't replace" philosophy.

**Technical Implications**:
- Kit metadata stored in `.agentii-kit.yml` manifest files in repos
- Platform indexes kits via GitHub API or webhooks
- "Submit a kit" flow is "connect your GitHub repo"
- Kit updates automatically sync from GitHub commits
- Users fork kits via GitHub, not proprietary mechanisms

### V. Progressive Disclosure of Complexity

**Principle**: The platform MUST serve both novice users (who need hand-holding) and power users (who want full control), without frustrating either.

**Requirements**:
- User stories MUST specify user sophistication levels (beginner, intermediate, expert)
- Plans MUST include progressive UI complexity (simple defaults, advanced options hidden)
- Tasks MUST implement tiered documentation (quickstart, full docs, advanced guides)
- Research MUST segment users by technical proficiency and validate separate flows
- Hypotheses MUST test whether simplified onboarding increases conversion without degrading expert experience

**Rationale**: Product Managers and Marketers (target users) have lower Git fluency than software engineers. The platform must abstract complexity without removing power.

**Experience Tiers**:
- **Tier 1 (Browse)**: No GitHub account, explore kits as public gallery
- **Tier 2 (Use)**: GitHub account, "fork to use" one-click workflows
- **Tier 3 (Customize)**: Edit `.specify/` files via web UI or local clone
- **Tier 4 (Create)**: Build kits from scratch, submit to marketplace
- **Tier 5 (Maintain)**: Manage multiple kits, respond to community, featured creator

### VI. Measurable Learning Velocity

**Principle**: PMF discovery MUST prioritize speed of learning over speed of building. Ship experiments, not features.

**Requirements**:
- Specs MUST frame features as hypotheses, not requirements ("We believe X will cause Y")
- Plans MUST include smallest viable experiments (landing page before app, mockup before code)
- Tasks MUST sequence research before implementation (validate demand before building supply)
- Success criteria MUST include learning objectives, not just delivery milestones
- Experiments MUST have explicit "kill" criteria (when to stop investing)

**Rationale**: Most marketplaces fail because they build the wrong thing. Fast learning enables fast pivots before sunk costs accumulate.

**Experiment Examples**:
- Landing page + waitlist → Test value prop messaging
- Figma mockups + user interviews → Test navigation and discovery flows
- Manual curation (Airtable) → Test quality standards before automating
- Single domain vertical (PM-Kit only) → Test depth before breadth

### VII. Monetization-Aware Architecture

**Principle**: While initial focus is PMF, the platform architecture MUST NOT preclude future business models.

**Requirements**:
- Specs MUST document potential monetization paths (even if not implemented yet)
- Plans MUST avoid technical decisions that lock out future revenue models
- Tasks MUST instrument analytics for signals predictive of willingness-to-pay
- Research MUST probe user and creator willingness to pay (even if product is free now)
- Hypotheses MUST test premium features or tiers alongside free offerings

**Rationale**: Many successful products discovered monetization late but had to rebuild. agentii-kit should keep options open without premature optimization.

**Potential Models** (not committed, keep optionality):
- **Freemium**: Basic kits free, advanced/private kits paid
- **Creator Monetization**: Kit creators charge for premium kits, platform takes cut
- **Enterprise Tier**: Private kit repositories, team management, SSO
- **Sponsorship**: Featured kit placements, brand integrations
- **Education**: Cohort-based courses teaching kit creation

## PMF-Specific Quality Standards

### Research Quality

- Interviews MUST be with real target users (not friends/family proxies)
- Quotes MUST be verbatim and attributed (anonymize if needed, but keep context)
- Sample sizes MUST be documented with selection methodology
- Contradictory evidence MUST be reported (not just confirming quotes)
- User actions MUST outweigh user statements ("watch what they do, not what they say")

### Hypothesis Quality

- Hypotheses MUST specify WHO (persona), WHAT (behavior), WHY (motivation), and MEASURE (metric)
- Hypotheses MUST be independently testable (not bundled)
- Riskiest assumptions MUST be tested first
- Success thresholds MUST be defined before experiments run
- Alternative explanations MUST be considered for positive results

### Evidence Quality

- Behavioral evidence (GitHub stars, forks, actual kit usage) beats survey data
- Paying customers (future state) beat free users beat prospects
- Recent behavior beats historical behavior beats stated intent
- Consistent patterns across multiple user cohorts required
- Negative signals (churn, low engagement) MUST be investigated, not ignored

## Development Workflow

### Phase 0: Constitution (Completed)

This document establishes governing principles for agentii-kit website PMF discovery. Project-specific additions:
- Target market: Knowledge workers using AI agents (PMs, marketers, educators, legal ops)
- PMF definition: 40% of surveyed users would be "very disappointed" if agentii-kit disappeared (Sean Ellis test)
- Research methods: Customer development interviews, landing page tests, prototype usability studies
- Privacy compliance: GDPR-compliant analytics, no PII in public GitHub repos
- Decision framework: RICE prioritization (Reach, Impact, Confidence, Effort)

### Phase 1: Specification (/pmfkit.specify)

Define WHAT we're learning and WHY. For agentii-kit:
- Learning objectives: "Do kit creators exist? Will they contribute? Will users adopt kits?"
- Target segments: Kit creators (domain experts) vs. Kit users (practitioners)
- Hypotheses: Supply-side (creator value props) vs. Demand-side (user value props)
- Success criteria: Activation, engagement, retention, referral metrics for both sides
- Edge cases: Quality control, spam prevention, GitHub integration failures

Do NOT specify technical stack at this phase.

### Phase 2: Clarification (/pmfkit.clarify)

Before planning, run structured clarification to identify gaps:
- Who are the "best first customers" for each side of the marketplace?
- What is the minimum viable kit quality standard?
- How will we source initial kit supply (cold start problem)?
- What GitHub integration depth is required for MVP?
- How do we measure "job kit usefulness" quantitatively?

### Phase 3: Planning (/pmfkit.plan)

Define HOW we'll execute discovery. For agentii-kit:
- Phase 1: Landing page + interview recruitment (validate problem)
- Phase 2: Figma prototype + usability tests (validate solution)
- Phase 3: Curated gallery MVP (validate product)
- Phase 4: Creator self-service submission (validate scale)
- Tech stack: Next.js, GitHub API, Vercel deployment (defer database until Phase 4)

### Phase 4: Task Breakdown (/pmfkit.tasks)

Generate actionable, dependency-ordered tasks:
- **Phase 1 Tasks**: Landing page copywriting, waitlist form, outreach scripts, interview guides
- **Phase 2 Tasks**: User flows, mockup designs, prototype builds, testing sessions
- **Phase 3 Tasks**: Curated kit selection, content migration, MVP development, launch
- **Phase 4 Tasks**: Submission flow, moderation tools, analytics instrumentation

Tasks MUST be grouped by learning objective with independent validation checkpoints.

### Phase 5: Execution (/pmfkit.implement)

Execute tasks systematically:
- Hypothesis → Experiment design → Data collection → Analysis → Decision
- Validate at each checkpoint (Phase 1 before Phase 2, etc.)
- Document evidence continuously in spec.md "Learnings" section
- Update plans based on invalidated hypotheses
- Decide continue/pivot/expand based on evidence

## Governance

### Amendment Procedure

1. Propose changes via pull request to `.specify/memory/constitution.md`
2. Document rationale and impact in Sync Impact Report (HTML comment at top)
3. Update version following semantic versioning (see below)
4. Validate all templates for consistency (checklist in report)
5. Update dependent documentation
6. Require project maintainer sign-off

### Versioning Policy

- **MAJOR (X.0.0)**: Principle removal, incompatible governance changes
- **MINOR (0.X.0)**: New principles, expanded sections, new workflows
- **PATCH (0.0.X)**: Clarifications, typo fixes, non-semantic changes

### Compliance Review

- All specs MUST reference constitution principles explicitly
- All plans MUST pass Constitution Check gates (validate against principles)
- All PRs MUST verify compliance with constitution
- Non-compliance MUST be explicitly justified with rationale
- AI agents MUST validate against constitution before generation

### Constitution Inheritance

agentii-kit website constitution inherits from PMF-Kit, which inherits from spec-kit:

**Inherited from PMF-Kit**:
- Specification-first approach
- Customer-evidence-driven validation
- Iterative validation cycles
- Minimal viable process
- Cross-functional integration
- Kit namespace isolation (`pmfkit.*` commands)
- Template extensibility

**Adapted for agentii-kit**:
- Two-sided marketplace principles (creators + users)
- Community-first discovery
- Content quality standards
- GitHub-native distribution
- Progressive disclosure for non-technical users
- Measurable learning velocity
- Monetization-aware architecture

**Project-Specific**:
- Target users: Knowledge workers using AI agents (PMs, marketers, educators)
- Domain: Job Kit marketplace and discovery platform
- Visual identity: "GitHub Geek with a Twist" design system (dark mode, teal accents)
- Distribution: kits.agentii.ai (Vercel deployment, GoDaddy DNS)
- Competition: PromptBase, Fabric, Cursor Rules repositories (see refs/competitors.md)

### Living Document

This constitution MUST evolve as agentii-kit discovers PMF:
- Incorporate learnings from customer interviews and experiments
- Refine principles based on validated/invalidated hypotheses
- Add marketplace-specific patterns as they emerge
- Maintain consistency with upstream PMF-Kit and spec-kit innovations
- Balance standardization (process consistency) with flexibility (pivot capability)

## Project Context

### Current Status

- **Phase**: Pre-launch PMF discovery
- **Target Launch**: Q1 2026 (tentative, contingent on validation)
- **Team**: Solo founder (early stage)
- **Resources**: Bootstrap budget, no VC funding yet
- **Assets**: Domain (agentii.ai), brand name, competitive research, design system

### Key Resources

- **refs/overview.md**: Spec-kit analysis and Job Kit concept validation
- **refs/competitors.md**: Competitive landscape (Cursor Rules, Fabric, PromptBase)
- **refs/graphic_designs.md**: Visual identity and UI design system
- **refs/deploy.md**: Vercel + GoDaddy DNS deployment guide
- **refs/README_spec-kit.md**: Upstream spec-kit documentation and philosophy

### Success Definition

**agentii-kit achieves product-market-fit when**:
1. **Creator PMF**: 20+ high-quality kits submitted by domain experts (not just developers)
2. **User PMF**: 1000+ monthly active users browsing and forking kits
3. **Engagement**: 40% weekly active user retention rate (returning users)
4. **Sean Ellis Test**: 40%+ of users "very disappointed" if platform disappeared
5. **Network Effects**: Each new kit drives measurable increase in user acquisition
6. **Creator Retention**: 50%+ of kit creators submit a second kit within 90 days
7. **Cross-Side Conversion**: 10%+ of users become kit creators
8. **Organic Growth**: 30%+ of new users arrive via word-of-mouth/referral

These metrics will be refined as we learn more about user behavior.

### Non-Goals (Explicit Scope Limits)

To maintain focus during PMF discovery, agentii-kit will NOT:
- Build proprietary AI agents (we index kits for existing agents like Claude Code)
- Create our own kit templates (we curate community-created kits)
- Compete with GitHub (we augment GitHub, not replace it)
- Target software engineers exclusively (we serve all knowledge workers)
- Monetize before PMF (focus on usage, not revenue, until market pull exists)
- Support non-GitHub hosting initially (GitHub-only for MVP simplicity)

**Version**: 2.0.0 | **Ratified**: 2025-12-04 | **Last Amended**: 2025-12-04
