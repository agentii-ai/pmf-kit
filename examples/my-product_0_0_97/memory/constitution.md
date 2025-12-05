<!--
SYNC IMPACT REPORT
==================
Version: 1.1.0 → 2.0.0 (MAJOR UPDATE - Agentii-Kit Marketplace)
Rationale: Complete transformation from PMF-Kit to Agentii-Kit marketplace platform

Changes in This Version:
- MAJOR: Redefined all principles for marketplace context (from PMF discovery to kit marketplace)
- MAJOR: Changed project focus from product-market-fit validation to marketplace platform
- MAJOR: New governance model for two-sided marketplace (providers + users)
- Added Principle: Kit Quality Standards (marketplace-specific)
- Added Principle: Provider Enablement (creator success)
- Added Principle: Discovery & Curation (user experience)
- Modified: Namespace from pmfkit.* to agentiikits.* commands
- Modified: Workflow phases from PMF research to marketplace operations
- Modified: Success metrics from customer validation to marketplace metrics (GMV, active kits, retention)
- Added: GitHub integration requirements (all kits must be GitHub-based)
- Added: Multi-agent compatibility as core quality standard

Project Context:
- Platform: Open-source marketplace for spec-kit-like job kits
- Users: Kit providers (creators) and kit consumers (users/implementers)
- Core Value: "Fork to Work" - Don't start from scratch, fork and customize
- Competitive Position: Blue Ocean opportunity vs. closed ecosystems (Notion, Asana)
- Technical Foundation: Based on spec-kit architecture, extending beyond code to all knowledge work

Templates Requiring Updates:
- ⚠ .pmf/templates/plan-template.md - Needs marketplace-specific planning sections
- ⚠ .pmf/templates/spec-template.md - Needs two-sided marketplace perspective (provider + user)
- ⚠ .pmf/templates/tasks-template.md - Needs marketplace operation task categories
- ⚠ All command files - Need agentiikits.* namespace updates

Follow-up TODOs:
- Update all command files to use agentiikits.* prefix (not pmfkit.*)
- Create kit submission/curation workflow documentation
- Define kit quality scoring rubric (completeness, documentation, multi-agent support)
- Build provider onboarding guide
- Define user discovery and search taxonomy
- Create marketplace metrics dashboard specifications
-->

# Agentii-Kit Constitution

## Preamble

**Agentii-Kit** is an open-source marketplace for **job kits**—structured, AI-agent-ready templates that help professionals accomplish complex work across domains (marketing, product management, legal, education, startups, etc.). This platform enables kit **providers** (creators) to share reusable workflows and **users** (implementers) to discover, fork, and execute these workflows with AI assistance.

**Purpose**: Build a thriving two-sided marketplace where creators can publish high-quality job kits and users can find "agent-ready" solutions that eliminate the blank-page problem across all knowledge work—not just coding.

**Scope**: This constitution governs the development and operation of the agentii-kit marketplace platform, establishing principles for kit quality, provider enablement, user discovery, technical standards, and platform governance.

**Heritage**: Agentii-kit extends the [spec-kit](https://github.com/github/spec-kit) architecture beyond software development to all structured knowledge work, validating the core insight that spec-driven workflows are domain-agnostic.

## Core Principles

### I. Marketplace-First Thinking

**Principle**: Every platform decision MUST optimize for both kit providers (supply) and kit users (demand). Single-sided optimization is forbidden.

**Requirements**:
- Feature specifications MUST include provider impact AND user impact sections
- Success metrics MUST track both supply health (kit submissions, creator retention) AND demand health (kit downloads, user success rate)
- UX designs MUST address both creator and consumer workflows
- Platform policies MUST balance creator freedom with user safety/quality
- Technical architecture MUST support provider customization AND user discoverability

**Rationale**: Marketplaces live or die by network effects. Favoring one side over the other creates imbalance and platform failure. GitHub succeeded by serving both code producers and consumers equally well.

### II. Kit Quality Standards (Non-Negotiable)

**Principle**: All kits in the marketplace MUST meet minimum quality thresholds to prevent "template pollution" and maintain user trust.

**Requirements**:
- **Completeness**: Every kit MUST include all four core files:
  - `constitution.md` (domain principles and constraints)
  - `spec-template.md` (requirements structure)
  - `plan-template.md` (implementation approach)
  - `tasks-template.md` (actionable breakdown)
- **Documentation**: Every kit MUST have a README explaining:
  - What job it solves
  - Who it's for (target user persona)
  - Example use cases
  - Setup instructions
  - Multi-agent compatibility status
- **GitHub Integration**: Every kit MUST be GitHub-hosted with:
  - Valid repository link
  - Open-source license (MIT, Apache, CC BY)
  - Version tagging (semantic versioning)
- **Multi-Agent Compatibility**: Kits MUST specify:
  - Tested AI agents (Claude Code, Cursor, Copilot, etc.)
  - Known limitations per agent
  - Minimum compatibility threshold (≥2 agents)
- **No Placeholders**: Templates MAY contain `[PLACEHOLDER]` tokens, but the README MUST explain what users should replace them with

**Rationale**: Low-quality templates erode trust and waste user time. GitHub's success with repositories required minimum standards (README, license, etc.). Agentii-kit adopts similar quality gates.

### III. Provider Enablement

**Principle**: The platform MUST make it trivially easy for domain experts (non-developers) to create, publish, and maintain kits.

**Requirements**:
- Kit submission workflow MUST NOT require coding skills
- Platform MUST provide:
  - Starter templates for each kit type
  - Validation tools (linting, completeness checks)
  - Preview/test environments
  - Usage analytics (downloads, stars, forks)
- Documentation MUST include:
  - "Your First Kit" tutorial (< 30 min)
  - Best practices guide per domain (marketing-kit, pm-kit, legal-kit)
  - Monetization pathways (if applicable)
- Provider dashboard MUST show:
  - Kit performance metrics
  - User feedback/issues
  - Version adoption rates

**Rationale**: Supply-side friction kills marketplaces. If only developers can create kits, we limit supply to a tiny audience. The revolution happens when marketers, PMs, and lawyers can create kits themselves.

### IV. Discovery & Curation

**Principle**: Users MUST be able to find the right kit for their job within 60 seconds of landing on the platform.

**Requirements**:
- **Taxonomy**: Kits MUST be categorized by:
  - Job domain (Marketing, Product, Legal, Startup, Education, etc.)
  - Use case tags (e.g., "SEO", "Product Hunt Launch", "Contract Review")
  - Complexity level (Beginner, Intermediate, Advanced)
- **Search & Filter**: Platform MUST support:
  - Full-text search (kit names, descriptions, tags)
  - Multi-filter combinations (domain + agent + license)
  - Sort options (most popular, recently updated, most starred)
- **Quality Signals**: Each kit card MUST display:
  - Star/like count (social proof)
  - Last updated date (freshness)
  - Multi-agent compatibility badges
  - Creator reputation score (if applicable)
- **Curation**: Platform MAY feature:
  - "Editor's Choice" collections
  - "Trending this week" section
  - Domain-specific curated lists

**Rationale**: Discovery is the hardest problem in content marketplaces. GitHub solved this with stars, forks, and trending repos. Agentii-kit adapts these patterns for job kits.

### V. GitHub-Native Architecture

**Principle**: Agentii-kit is NOT a walled garden. All kits MUST live on GitHub, and the marketplace is a discovery/curation layer on top of the open-source ecosystem.

**Requirements**:
- Platform MUST NOT host kit files directly (reference GitHub repos only)
- Kit pages MUST link prominently to source GitHub repository
- Users MUST be able to fork kits via GitHub workflows
- Platform MUST sync kit metadata from GitHub (README, stars, contributors, last commit)
- Kit updates MUST pull from GitHub (not re-uploaded to platform)

**Rationale**: This prevents platform lock-in and aligns with the open-source ethos. Users own their kits. Agentii-kit is a Lens on GitHub, not a vault.

### VI. Multi-Agent Compatibility

**Principle**: Kits MUST work across multiple AI agents, not just one. Vendor lock-in is forbidden.

**Requirements**:
- Kit documentation MUST list tested agents (minimum 2)
- Platform MUST display compatibility badges on kit cards
- Kits MAY provide agent-specific setup instructions (e.g., `.claude/`, `.cursor/`)
- Platform MUST aggregate compatibility data across kits (e.g., "90% of PM-kits support Claude Code")
- Kit creators MUST disclose if a kit is agent-exclusive (and justify why)

**Rationale**: The AI agent landscape is fragmented. Users switch agents frequently. Kits that lock users to one agent create friction and reduce adoption. Cross-agent compatibility is a competitive advantage.

### VII. "Fork to Work" Philosophy

**Principle**: Users should NEVER start from a blank page. Every job has a starting template.

**Requirements**:
- Landing page MUST emphasize "Don't start from scratch, fork and customize"
- Kit cards MUST have prominent "Fork to GitHub" button
- Platform MUST provide:
  - One-click fork workflows
  - Pre-populated setup instructions
  - Example customizations (before/after comparisons)
- Documentation MUST explain:
  - How to customize `constitution.md` for their org
  - How to adapt `spec-template.md` for their use case
  - When to create a new kit vs. fork an existing one

**Rationale**: This is the killer feature. Notion templates failed because they're not forkable or version-controlled. GitHub repos are forkable but lack job-specific structure. Agentii-kit combines both.

### VIII. Spec-Driven Workflow Consistency

**Principle**: All kits MUST follow the 4-file spec-driven architecture inherited from spec-kit. Variations are allowed only with explicit justification.

**Requirements**:
- Every kit MUST include:
  - `constitution.md` (domain rules and constraints)
  - `spec-template.md` (requirements structure)
  - `plan-template.md` (implementation plan)
  - `tasks-template.md` (task breakdown)
- Kits MAY add supplementary files (e.g., `research.md`, `contracts/`, `examples/`)
- Kits MUST NOT omit core files without documented rationale
- Platform MUST validate file presence during submission

**Rationale**: Consistency enables transferable skills. A user who learns one kit can navigate any other kit. This structural standardization is what made GitHub repos intuitive despite infinite content variety.

### IX. Namespace Isolation

**Principle**: Agentii-kit MUST coexist with other kit variants (spec-kit, pmf-kit, marketing-kit) without naming conflicts.

**Requirements**:
- CLI command MUST be `agentiikits` (not `specify` or `pmf`)
- Slash commands MUST use `agentiikits.*` prefix:
  - `/agentiikits.constitution`
  - `/agentiikits.specify`
  - `/agentiikits.plan`
  - `/agentiikits.tasks`
  - `/agentiikits.implement`
- Templates MUST reference correct command namespaces
- Documentation MUST explain multi-kit installation strategy

**Rationale**: Users may install multiple kit variants on the same system. Unique namespaces prevent conflicts and enable specialized workflows to coexist.

### X. Accessibility & Inclusivity

**Principle**: The platform MUST be usable by non-developers, including marketers, PMs, lawyers, educators, and creatives.

**Requirements**:
- UI/UX MUST meet WCAG AA standards
- Language MUST avoid developer jargon (e.g., "fork" → explain as "make your own copy")
- Documentation MUST include non-technical examples
- Kit categories MUST include non-coding domains (marketing, legal, education)
- Platform MUST NOT assume terminal/command-line familiarity in the core user flows

**Rationale**: Agentii-kit's differentiation is bringing spec-driven workflows to ALL knowledge work, not just coding. If the platform feels "developers only," we fail the mission.

## Marketplace Quality Standards

### Kit Submission Requirements

- **Metadata Completeness**:
  - Title (≤60 chars)
  - Description (≤200 chars)
  - Long description (≥300 words)
  - Category (from approved taxonomy)
  - Tags (3-10 tags)
  - License (valid open-source license)
  - Multi-agent compatibility list (≥2 agents tested)

- **File Structure Validation**:
  - All four core files present (`constitution.md`, `spec-template.md`, `plan-template.md`, `tasks-template.md`)
  - README.md present with required sections
  - No broken links in documentation
  - Valid GitHub repository URL

- **Content Quality**:
  - No Lorem Ipsum placeholders in core documentation
  - At least one example use case provided
  - Instructions tested by at least one external user (beta tester)

### Provider Reputation System

- **Reputation Score** (0-100):
  - +10 per kit published
  - +5 per star received
  - +3 per fork
  - +2 per successful user implementation (verified via feedback)
  - -5 per unresolved issue (open >30 days)
  - -10 per kit removal due to quality violations

- **Reputation Tiers**:
  - **Newcomer** (0-50): Default badge
  - **Contributor** (51-150): Blue badge
  - **Expert** (151-300): Purple badge
  - **Legend** (301+): Gold badge, featured placement

### User Success Metrics

- **Kit Effectiveness**:
  - Time to first successful use (target: <60 minutes)
  - Completion rate (% of users who finish all tasks)
  - User rating (1-5 stars)
  - Repeat usage rate (same user, multiple times)

- **Platform Health**:
  - Monthly active kits (MAK): Kits downloaded/forked in last 30 days
  - Provider retention rate (% still active after 6 months)
  - User retention rate (% who fork ≥2 kits)
  - Gross Marketplace Value (GMV): Total value created (if monetization added)

## Development Workflow

### Phase 0: Constitution (Marketplace Governance)

Use `/agentiikits.constitution` to establish platform-specific principles:
- Target user personas (kit creators vs. kit consumers)
- Kit quality thresholds
- Moderation policies
- Growth metrics and targets
- Technical architecture constraints

### Phase 1: Specification (/agentiikits.specify)

Define WHAT marketplace features to build. Focus on:
- User stories for BOTH providers and consumers
- Two-sided success criteria (supply + demand)
- Edge cases (spam kits, low-quality submissions, copyright issues)
- Competitive positioning vs. Notion, Asana, GitHub alone

Do NOT specify tech stack at this phase.

### Phase 2: Clarification (/agentiikits.clarify)

Before planning, run structured clarification:
- Ambiguous user flows (especially for non-developers)
- Unclear success metrics (supply-side vs. demand-side)
- Missing validation criteria (kit quality thresholds)
- Unstated assumptions (GitHub familiarity, AI agent access)

### Phase 3: Planning (/agentiikits.plan)

Define HOW to build the marketplace. Specify:
- Technical architecture (web app, API, database)
- Kit ingestion pipeline (GitHub sync, validation, metadata extraction)
- Search and discovery implementation (indexing, filters, ranking algorithm)
- Provider and user dashboards
- Analytics and instrumentation

### Phase 4: Task Breakdown (/agentiikits.tasks)

Generate actionable, dependency-ordered tasks:
- Frontend UI components (kit cards, search, filters)
- Backend services (kit validation, GitHub sync, user auth)
- Database schema (kits, providers, users, analytics)
- Testing (multi-agent compatibility, UX testing with non-devs)

Tasks MUST be grouped by user story with independent validation checkpoints.

### Phase 5: Execution (/agentiikits.implement)

Execute tasks systematically:
- Follow TDD equivalent: Spec → Implementation → Validation
- Validate at each checkpoint (provider + user perspectives)
- Document evidence continuously
- Update specs based on learnings
- Decide continue/pivot based on criteria

### Phase 6: Launch & Iteration

After initial marketplace launch:
- Monitor supply/demand balance (kit submissions vs. downloads)
- Collect user feedback (NPS surveys, usage analytics)
- Iterate on discovery algorithms (A/B test ranking criteria)
- Expand kit taxonomy based on demand signals
- Build creator community (forums, showcase, events)

## Governance

### Amendment Procedure

1. Propose changes via pull request to `.pmf/memory/constitution.md`
2. Document rationale and impact in Sync Impact Report
3. Update version following semantic versioning
4. Validate all templates for consistency
5. Update dependent documentation
6. Require sign-off from project maintainers

### Versioning Policy

- **MAJOR (X.0.0)**: Principle removal, incompatible governance changes, marketplace model shifts
- **MINOR (0.X.0)**: New principles, expanded sections, new workflows
- **PATCH (0.0.X)**: Clarifications, typo fixes, non-semantic changes

### Compliance Review

- All specs MUST reference constitution principles
- All plans MUST pass Constitution Check gates
- All PRs MUST verify compliance
- Non-compliance MUST be explicitly justified in Complexity Tracking
- AI agents MUST validate against constitution before generation

### Marketplace Moderation

- **Kit Removal Criteria**:
  - Copyright violations (DMCA takedown)
  - Malicious content (phishing, malware, scams)
  - Repeated quality violations (unresolved for >60 days)
  - Spam or duplicate submissions
- **Appeal Process**:
  - Providers can appeal removal within 14 days
  - Review by platform maintainers
  - Decision final after review

### Living Document

This constitution MUST evolve as Agentii-kit grows:
- Incorporate learnings from provider and user feedback
- Refine principles based on marketplace dynamics (supply/demand imbalances)
- Add domain-specific patterns as new kit categories emerge
- Maintain consistency with upstream spec-kit innovations
- Balance standardization with creator flexibility

**Version**: 2.0.0 | **Ratified**: 2025-12-05 | **Last Amended**: 2025-12-05
