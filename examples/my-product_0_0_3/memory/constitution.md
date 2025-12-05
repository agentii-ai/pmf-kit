<!--
SYNC IMPACT REPORT
==================
Version: 1.0.0 → 2.0.0 (MAJOR: Platform Transformation)
Rationale: Transform from PMF-Kit reference implementation to agentii-kit marketplace platform for spec-kit variants

Version Change: MAJOR (1.0.0 → 2.0.0)
- Removed: PMF-specific principles (Principles II, III focused on customer discovery)
- Added: Marketplace infrastructure principles (Kit Curation, Developer Experience, Multi-Agent Support)
- Redefined: Core positioning from "PMF discovery tool" to "Open marketplace for AI agent job kits"
- Restructured: Core Principles to reflect marketplace/platform needs vs. single-use-case domain

Modified Principles:
- I. Specification-First → I. Kit-First Specification (repurposed for kit creators, not PMF users)
- II. Customer-Evidence-Driven → REMOVED (PMF-specific, replaced with Marketplace Quality)
- III. Iterative Validation → REMOVED (PMF-specific, replaced with Kit Discoverability)
- IV. Minimal Viable Process → IV. Minimal Viable Kit (adapted for kit design)
- V. Cross-Functional Integration → REMOVED (replaced with Multi-Kit Interoperability)
- VI. Kit Namespace Isolation → II. Kit Namespace Isolation (elevated; now core to marketplace)
- VII. Template Extensibility → III. Template Extensibility (now core principle)

Added Sections:
- Marketplace Quality Standards (replacing PMF research quality)
- Multi-Kit Interoperability (enabling cross-kit workflows)
- Kit Discoverability & Curation
- Developer Ecosystem (creator guidelines)
- Platform Neutrality (supporting all agent types)

Templates Requiring Updates:
- ✅ /templates/plan-template.md - Updated for kit development, not PMF discovery
- ✅ /templates/spec-template.md - Updated for kit specifications vs. research specs
- ✅ /templates/tasks-template.md - Updated for kit creation tasks
- ✅ /.claude/commands/*.md - Using pmfkit.* prefix for agentii-kit
- ⚠ CLI implementation (future) - Will use "agentii" or "kit" commands

Follow-up TODOs:
- Create kit-template-library.md with examples for common job kit types
- Develop kit validation and quality review process
- Build marketplace.md with kit discovery and curation guidelines
- Create contributor-guide.md for kit creators
- Establish versioning policy for published kits
- Design API/metadata schema for kit publishing

Domains Changed:
This constitution governs the agentii-kit PLATFORM (not a single kit variant).
Inherits spec-kit architecture but focuses on marketplace and kit ecosystem concerns.
-->

# agentii-kit Constitution: Marketplace for Spec-Kit Variants

## Preamble

**agentii-kit** is an open-source marketplace and framework for creating, sharing, and discovering spec-kit
variants tailored to specific jobs and domains. Rather than being a single domain-specific kit (like PMF-Kit,
Marketing-Kit, or Legal-Kit), agentii-kit is the **platform infrastructure** that enables anyone to build,
publish, and collaborate on specialized kits for AI agents like Claude Code, Cursor, and similar tools.

**Mission**: Enable a global community of experts to codify their domain knowledge into reusable, AI-agent-ready
job kits, transforming how professionals across all industries leverage structured workflows with AI.

**Scope**: This constitution governs:
- The marketplace platform itself (discovery, curation, publishing)
- Quality standards and validation for published kits
- Interoperability patterns between kits
- Developer experience for kit creators
- Agent neutrality and multi-agent support

**Vision**: A GitHub-like ecosystem where Marketing Directors, Legal Experts, Product Managers, Educators,
and Domain Specialists can fork, customize, and contribute to kits—just as developers fork code repositories.

## Core Principles

### I. Kit-First Specification

**Principle**: Every kit creation initiative MUST begin with a clear, reusable specification that codifies
domain knowledge into structured templates (constitution.md, spec.md, plan.md, tasks.md) suitable for
multi-agent execution.

**Requirements**:
- Kits MUST be templated and domain-agnostic enough to be forked and customized
- Domain-specific constraints MUST be encoded in the constitution.md
- Kit specifications MUST include guardrails and decision trees for domain practitioners
- Kit documentation MUST explain adaptation and customization patterns
- Quality gates MUST exist before publishing (peer review, validation checks)

**Rationale**: Spec-Driven Development is fundamentally about encoding expertise into executable structures.
A well-designed kit captures years of professional practice and makes it reproducible and shareable.

### II. Kit Namespace Isolation

**Principle**: Kits MUST coexist in the agentii-kit marketplace with zero naming conflicts and clear identity.

**Requirements**:
- Each kit MUST have a unique identifier: `<domain>-kit` (e.g., `marketing-kit`, `legal-kit`, `seo-kit`)
- CLI commands (future) MUST use namespace prefixes (e.g., `agentii kit:create`, `agentii kit:publish`)
- Slash commands (agent-level) MUST follow: `/agentiikits.specify`, `/agentiikits.plan`, etc.
- Package names MUST follow: `agentii-<domain>-kit` (npm, pip, etc.)
- Kit repositories MUST follow naming: `github.com/<org>/<domain>-kit`
- Documentation MUST clearly distinguish between:
  - The agentii platform (this constitution)
  - Individual kit variants (each with their own constitution)

**Implementation**:
```
agentii platform commands:
- agentii kit:search                   # Search marketplace
- agentii kit:fork <kit-id>           # Fork a kit
- agentii kit:validate <kit-path>      # Validate kit structure
- agentii kit:publish <kit-path>       # Publish to marketplace

Individual kit commands (within each kit):
- /marketing-kit.specify               # Kit-specific workflow
- /legal-kit.plan
- /seo-kit.tasks
```

**Rationale**: Multiple kits will co-exist on developers' machines. Clear namespace conventions prevent
conflicts and enable seamless discovery and switching between specialized workflows.

### III. Template Extensibility & Kit Composability

**Principle**: agentii-kit serves as the reference platform implementation demonstrating how spec-driven
methodologies extend beyond software engineering to ANY domain. Kits must be composable and extensible.

**Requirements**:
- Base kit templates MUST be framework-agnostic
- Kits MUST document how to adapt and extend for new domains
- Cross-kit workflows MUST be possible (e.g., Marketing-Kit reads Product-Kit spec.md)
- The platform MUST support kit inheritance and dependency chains
- Kit creators MUST follow standard patterns for customization
- Examples MUST show real-world kit adaptations

**Rationale**: By building a composable platform, agentii-kit becomes a force multiplier. One well-designed
kit unblocks dozens of adjacent domains. Professional communities (marketing, legal, education, finance,
healthcare) can each own and evolve their kits independently while benefiting from platform improvements.

### IV. Minimal Viable Kit (MVK)

**Principle**: Kit creators MUST design for simplicity and reusability. Complexity MUST be explicitly justified.

**Requirements**:
- Kits MUST define a Minimal Viable Kit with core templates only
- Extended features MUST be optional add-ons, not required
- Kit README MUST explain what's core vs. optional
- Documentation MUST include configuration examples for common scenarios
- MVK MUST be testable with sample data in under 15 minutes
- Kit complexity MUST be scored and documented

**Rationale**: Complex kits have high barriers to adoption. A simple, well-documented kit will be forked
and extended more than a feature-rich one that requires expert-level understanding.

### V. Marketplace Quality & Curation Standards

**Principle**: All published kits MUST meet quality standards ensuring professional utility, clarity, and
reliability.

**Standards for Kit Publication**:

**Documentation Quality**:
- README MUST explain kit purpose, target user, and primary use cases
- constitution.md MUST be clear and testable
- Example workflows MUST be included (at least 2–3 realistic scenarios)
- Troubleshooting guide MUST address common adaptation questions

**Specification Quality**:
- Templates MUST be concise and unambiguous
- Placeholder tokens MUST be documented (e.g., `[COMPANY_NAME]`, `[RISK_TOLERANCE]`)
- Field descriptions MUST be 1–2 sentences with examples
- Success criteria MUST be measurable and domain-specific

**Workflow Completeness**:
- All phases (constitution → specify → plan → tasks → implement) MUST be covered
- Cross-phase dependencies MUST be documented
- Checkpoint validation MUST be defined for each phase
- Sample outputs MUST be provided

**Validation Checklist**:
- [ ] Kit has unique, descriptive name (e.g., `content-strategy-kit`)
- [ ] constitution.md defines 5–7 core principles with rationale
- [ ] spec.md template includes placeholders with examples
- [ ] plan.md template includes phase definitions and deliverables
- [ ] tasks.md template is testable with provided sample data
- [ ] README includes at least one complete worked example
- [ ] Kit has been validated with 2+ independent users outside creator's team
- [ ] Kit is backward-compatible with spec-kit 1.x architecture

**Discoverability**:
- Kits MUST be tagged by domain and primary agent support (Claude, Cursor, etc.)
- Kits MUST include search keywords in metadata
- Kits MUST specify target personas and use cases
- Kits MUST be ranked by adoption and community ratings

**Rationale**: Professional users trust only vetted, well-documented resources. Curation maintains quality
and ensures the agentii-kit marketplace is a destination for serious domain work, not a collection of
half-finished experiments.

### VI. Multi-Agent Interoperability

**Principle**: Kits MUST be designed to work with any AI agent platform that supports slash commands and file-based
workflows (Claude Code, Cursor, Copilot, Gemini, etc.).

**Requirements**:
- Kits MUST NOT assume a specific agent implementation
- Kit commands MUST use generic, agent-agnostic patterns (no Claude-specific hooks)
- File-based workflows (reading spec.md, writing tasks.md) MUST be the primary integration point
- Agent-specific adaptations (if any) MUST be optional overlays
- Kits MUST document which agents have been tested and verified
- Multi-agent testing MUST be part of the publication validation

**Rationale**: The more agents a kit supports, the broader its adoption and impact. Designing for interoperability
ensures kits remain relevant as the AI agent landscape evolves.

### VII. Kit Discoverability & Community Contribution

**Principle**: The marketplace MUST make it easy to discover, fork, adapt, and contribute to kits.

**Requirements**:
- Kits MUST be discoverable by domain, task, and use case
- "Fork this kit" workflow MUST be one-click or clearly documented
- Kit modification MUST preserve provenance (forks should reference parent kits)
- Contribution workflows MUST be defined (pull requests to official kits, community variants)
- Kit ratings and feedback systems MUST be transparent
- Version control and release notes MUST be clear (semantic versioning)

**Rationale**: GitHub's success comes from low friction for discovery and contribution. agentii-kit applies
the same principle to non-code domains.

## Marketplace Platform Architecture

### Base Kit Structure

Every published kit MUST follow this minimal structure:

```
<domain>-kit/
├── README.md                          # Kit overview, examples, target users
├── LICENSE                            # Open-source license (MIT/Apache/GPL variants)
├── .git/                              # Version control
├── .agentii/
│   ├── memory/
│   │   └── constitution.md            # Kit's own governing principles
│   ├── templates/
│   │   ├── spec-template.md           # Domain-specific spec template
│   │   ├── plan-template.md           # Domain-specific plan template
│   │   └── tasks-template.md          # Domain-specific tasks template
│   └── examples/
│       ├── example-1-spec.md          # Complete worked example
│       ├── example-1-plan.md
│       └── example-1-tasks.md
├── docs/
│   ├── adaptation-guide.md            # How to customize for other contexts
│   ├── faq.md
│   └── troubleshooting.md
└── .cursorrules (or .cursor/rules.mdc) # Optional: Cursor-specific adaptations
```

### Kit Validation Gates

Before publication, kits MUST pass:

1. **Structure Validation**: Correct file hierarchy, no missing required fields
2. **Documentation Audit**: README, examples, and docs meet quality bar
3. **Template Validation**: Templates are parseable, have proper placeholders
4. **Workflow Testing**: Complete cycle (constitution → specify → plan → tasks) runs without errors
5. **Use Case Testing**: At least 2–3 realistic scenarios execute successfully
6. **Community Review**: At least 2 independent reviews from domain experts (outside creator's team)

### Cross-Kit Workflows

Kits MAY define integration points with other kits:

Example: `marketing-kit` reads `product-kit`'s spec.md to understand product details before creating marketing plans.

**Requirements for cross-kit integration**:
- Integration MUST be documented and optional (kits work independently too)
- File contracts MUST be explicit (e.g., "expects `product-kit/specs/*/spec.md` in standard format")
- Graceful degradation MUST occur if dependent kit is absent
- Version compatibility MUST be documented

## Development Workflow for Kit Creators

### Phase 1: Conceptualization

Define:
- **Problem**: What job does this kit help professionals solve?
- **Audience**: Who are the primary users? (e.g., "Legal in-house counsel for SaaS startups")
- **Success Metric**: What does success look like? (e.g., "Save 10 hours/month on contract review")
- **Differentiation**: Why is this kit unique compared to existing tools/processes?

### Phase 2: Foundation (`constitution` for the kit)

Create your kit's governing principles using the `/agentiikits.constitution` command:

```
/agentiikits.constitution
Create a constitution for a [DOMAIN] kit focused on [PRIMARY_PROBLEM].
Domain experts: [WHO_VALIDATES]. Core workflows: [LIST_KEY_WORKFLOWS].
Compliance needs: [REGULATORY/CONSTRAINT_DETAILS].
```

Output: Kit-specific `constitution.md` (5–7 principles adapted to the domain)

### Phase 3: Specification Template Design

Define what inputs domain practitioners MUST specify. Example for a Legal-Kit:

```
/agentiikits.specify
Create a specification template for [LEGAL_SCENARIO].
Required inputs: [COUNTERPARTY_DETAILS], [RISK_TOLERANCE], [JURISDICTION].
Success criteria: [CONTRACT_APPROVAL_TIMELINE], [REDLINE_COMPLETENESS].
```

### Phase 4: Planning & Task Breakdown

Define HOW domain work will be executed:

```
/agentiikits.plan
Define a plan template for [DOMAIN] work including phases, research tasks, and validation gates.
Tech stack (if applicable): [TOOLS_USED].
Integration points: [OTHER_KITS_OR_SYSTEMS].
```

### Phase 5: Validation & Publication

- Test kit with 2–3 independent users
- Gather feedback and iterate
- Publish to marketplace via GitHub PR to agentii-kit registry

## Quality Standards

### Principle Clarity

- Every principle MUST have a succinct name (e.g., "Customer-Centric Validation")
- Every principle MUST have a testable definition (no vague "should" language)
- Every principle MUST have explicit, numbered requirements
- Every principle MUST have a rationale explaining WHY it matters for this domain

### Documentation Clarity

- Technical jargon MUST be defined or avoided
- Examples MUST be concrete and realistic (not hypothetical)
- Placeholder names MUST be descriptive (e.g., `[RISK_TOLERANCE_LEVEL]` not `[VAR1]`)
- Guidance MUST specify success/failure criteria (not just "best practice")

### Template Usability

- Templates MUST be parseable by AI agents (valid Markdown/YAML)
- Templates MUST include inline comments explaining each section
- Template examples MUST show common variations
- Templates MUST fail gracefully if optional sections are omitted

## Governance

### Amendment Procedure for Platform

1. Kit creators or maintainers propose changes via issue/discussion
2. Community review period (7 days minimum)
3. Platform maintainers approve and document rationale
4. Changes propagated to kit validation checklist and template examples
5. Version bump of platform constitution

### Kit Governance (Within Each Kit)

Each kit's maintainer(s) own:
- Kit's own constitution.md amendments
- Template updates and refinements
- Community contributions and forks
- Versioning and deprecation decisions

Platform MUST NOT dictate kit-internal governance.

### Versioning Policy

**Platform Constitution**:
- **MAJOR (X.0.0)**: Principle removals or incompatible workflow changes
- **MINOR (0.X.0)**: New principles, expanded validation gates, new integration patterns
- **PATCH (0.0.X)**: Clarifications, typo fixes, example updates

**Individual Kits**: Follow own versioning policy (documented in their README)

### Compliance Review

- All new kits MUST reference this platform constitution
- All kits MUST pass validation checklist before publication
- All PRs to core agentii-kit MUST verify backward compatibility
- Non-compliance issues MUST be documented in kit's own constitution (with justification)
- Community can flag low-quality kits for review or delisting

### Living Platform

This constitution MUST evolve:
- Incorporate learnings from published kits
- Add new patterns as domains expand (finance, healthcare, legal, design, etc.)
- Maintain balance between standardization (for discovery) and flexibility (for specialization)
- Support new agent integrations as platforms emerge

## Platform Principles Summary

The agentii-kit platform succeeds when:

1. **Ease of Discovery**: Any professional can find a kit for their job in under 2 minutes
2. **Ease of Adaptation**: Any kit can be forked and customized in under 15 minutes
3. **Quality Assurance**: Every published kit is production-ready and reviewed by domain experts
4. **Multi-Domain Coverage**: At least one high-quality kit exists for the top 20 professional jobs (marketing, product, legal, finance, HR, etc.)
5. **Agent Agnostic**: Kits work with any major AI agent platform without modification
6. **Community Growth**: Active contributors creating new kits and improving existing ones
7. **Measurable Impact**: Users report time savings and improved quality of work using kits

---

**Version**: 2.0.0 | **Ratified**: 2025-12-04 | **Last Amended**: 2025-12-04
