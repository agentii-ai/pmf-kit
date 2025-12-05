# Agentii-Kit Marketplace Constitution

> **Version**: 1.0.0
> **Status**: Draft
> **Author**: Frank Chen (frank@agentii.ai)
> **Created**: 2025-12-05
> **Last Updated**: 2025-12-05

---

## Preamble

**Agentii-Kit** is an open-source marketplace platform for discovering, installing, and managing specialized AI agent toolkits (like PMF-Kit, PD-Kit, Marketing-Kit, etc.). Built on the foundations of [Spec-Kit](https://github.com/github/spec-kit), Agentii enables both *kit creators* and *kit users* to collaborate in a federated ecosystem where structured, spec-driven methodologies can be adapted across domains.

**Purpose**: Create a sustainable, community-driven marketplace that makes high-quality, domain-specific AI agent workflows accessible to practitioners across product management, design, engineering, marketing, and business domains.

**Vision**: A world where any organization can discover, customize, and implement proven methodologies (codified as "kits") without reinventing workflows for each new domain or team.

**Scope**:
- Platform for publishing, discovering, and installing kit variants
- Registry and package management for kit artifacts
- Community curation and quality standards
- Documentation and guidance for kit creators
- Federated governance model supporting multiple kit publishers

---

## Core Principles

### I. Accessibility-First Platform Design

**Principle**: Agentii-Kit MUST lower barriers to entry for both kit users and kit creators.

**Requirements**:
- Single-command installation (e.g., `agentii init <kit-name>`)
- No complex build tooling or devops knowledge required
- Visual kit discovery and browser experience
- Clear, beginner-friendly documentation
- Free tier with option to publish kits

**Rationale**: The broader audience beyond software engineers will only adopt structured methodologies if they're as simple to use as downloading an app. Friction kills adoption.

**Implementation**:
```bash
# Simple installation
agentii kit install pmf-kit
agentii kit install pd-kit
agentii kit install marketing-kit

# Or from web UI
# Visit agentii.ai, browse kits, click "Install"
```

### II. Open, Verifiable Quality Standards

**Principle**: All published kits MUST meet minimum quality criteria that users can inspect and verify.

**Requirements**:
- Every kit MUST have a public constitution.md
- Every kit MUST include reference examples
- Every kit MUST have passing template validation
- Every kit MUST document success metrics and sample outcomes
- Every kit publisher MUST identify themselves (organization, maintainer)

**Quality Scoring**:
```
Template Coverage:   ⭐⭐⭐⭐⭐  (spec, plan, tasks templates present)
Documentation:      ⭐⭐⭐⭐    (examples, /refs/, quick-start provided)
Community Rating:   ⭐⭐⭐⭐    (based on user reviews, 100+ installs)
Maintenance:        ⭐⭐⭐     (updates in last 6 months, responsive maintainers)
Adoption:           ⭐⭐      (10,000+ downloads on platform)
```

**Rationale**: Users need confidence in published kits. Public quality standards create trust and enable users to make informed choices between competing kits.

### III. Federated Kit Ecosystem

**Principle**: No single organization controls all kits. Agentii-Kit operates as a registry connecting independent kit publishers.

**Requirements**:
- Any organization can publish kits to the registry
- Kit publishers retain full control of their repositories
- Namespace isolation prevents naming conflicts (e.g., `pmf-kit`, `marketing-kit`)
- Publishers can use their own governance (MIT, Apache, proprietary, etc.)
- Multiple versions of same kit can coexist

**Kit Publisher Rights**:
- Control over kit content and updates
- Ability to set publishing pace and release schedule
- Option to discontinue or archive kits
- Authority over community discussions on their kit

**Kit Publisher Responsibilities**:
- Maintain constitution and governance documentation
- Respond to security issues within 30 days
- Provide basic user support (issues, discussions)
- Keep kit compatible with current Agentii platform version
- Update templates annually or as Agentii evolves

**Rationale**: A centrally-controlled toolkit ecosystem becomes a bottleneck and stifles innovation. Publishers need autonomy to evolve their kits independently while maintaining quality standards.

### IV. Interoperability and Composability

**Principle**: Kits MUST be able to reference and extend each other without conflicts.

**Requirements**:
- Each kit has unique command namespace (e.g., `/pmfkit.*`, `/marketing-kit.*`)
- Kits can declare optional dependencies on other kits
- Shared templates (e.g., constitution.md format) use common conventions
- Configuration allows users to install multiple kits simultaneously
- Child kits explicitly inherit from parent kit constitutions

**Kit Dependency Model**:
```yaml
# marketing-kit/kit.yml
name: marketing-kit
version: 1.0.0
depends_on:
  - pmf-kit: ">=0.1.0"

commands:
  - /marketing-kit.brief      # Base command
  - /marketing-kit.persona    # Extends /pmfkit.specify
  - /marketing-kit.campaign   # Extends /pmfkit.plan
```

**Rationale**: Complex methodologies often stack. Marketing teams use PMF frameworks + domain-specific extensions. Composable kits enable practitioners to build exactly the workflow they need.

### V. Community-Driven Curation

**Principle**: Kit discovery and quality are shaped by community input, not algorithmic ranking.

**Requirements**:
- Users can rate and review published kits
- Kits featured in "Collections" curated by domain experts
- Community moderators review kits for quality and authenticity
- Publish community guide-driven patterns (e.g., "PMF for SaaS", "Design Ops Workflows")
- Regular community showcases highlighting best practices

**Curation Mechanisms**:
```
Featured Collections:
- "Finding PMF for AI SaaS"          (curated by venture capitalists + founders)
- "Product Design Workflows"          (curated by design leaders)
- "Engineering Team Productivity"     (curated by engineering managers)
- "Marketing Operations"              (curated by marketing strategists)

Community Awards:
- Most Useful Kit (annual)
- Best Documentation
- Most Innovative
- Growing Adoption (new kit with >1000 installs in 6 months)
```

**Rationale**: Experts understand which methodologies work best for different contexts. Community curation scales better than centralized ranking and builds stronger network effects.

### VI. Privacy and Data Ethics

**Principle**: Agentii-Kit MUST operate with full transparency and minimal data collection.

**Requirements**:
- No personal data collection from kit usage
- Download statistics shared transparently (public)
- User surveys fully opt-in (not required for kit use)
- No telemetry in installed kits (users own their data)
- Clear privacy policy and data retention (30 days max for logs)
- GDPR/CCPA compliance built-in from day one

**Data Governance**:
- Kit publishers NEVER receive information about who installed their kit
- Users can download kits without account (anonymous downloads supported)
- Kit usage analytics stored locally only (not synced to Agentii servers)
- Export of personal research data always user-controlled

**Rationale**: Practitioners in sensitive domains (law, healthcare, finance) need assurance their research data isn't collected or sold. Trust is foundational.

### VII. Kit Creator Enablement

**Principle**: Creating and publishing a kit MUST be as simple as possible, with extensive guidance.

**Requirements**:
- "Create Kit" wizard on agentii.ai
- Template starter kit with minimal viable structure
- Comprehensive /refs/ guide for kit creators
- Auto-generation of README.md and documentation
- Free CI/CD pipeline for template validation
- Versioning and release workflow templates

**Creator Resources**:
```
docs/
├── getting-started/
│   ├── create-your-first-kit.md
│   ├── kit-anatomy.md
│   └── publishing-checklist.md
├── advanced/
│   ├── multi-kit-dependencies.md
│   ├── custom-commands.md
│   └── localization.md
└── examples/
    ├── minimal-kit/
    ├── vertical-industry-kit/
    └── enterprise-governance-kit/
```

**Rationale**: The ecosystem thrives when barriers to entry are low. Investing in creator enablement pays exponential returns through increased innovation and competition.

### VIII. Sustainability and Governance

**Principle**: Agentii-Kit MUST establish clear governance enabling long-term platform sustainability.

**Requirements**:
- Core platform maintained by dedicated team
- Annual community RFC process for major changes
- Kit publisher advisory board (5-7 representatives)
- User council (10-15 active community members)
- Public roadmap and budget transparency
- Support for kit maintenance (grants, sponsorships for active publishers)

**Governance Structure**:
```
Agentii Board (steering)
├── Core Platform Team (development, infrastructure)
├── Kit Publisher Advisory (kit maintainers)
├── User Council (active community members)
└── Community Moderators (review, support)
```

**Revenue Model**:
- Free kit discovery and installation (open source forever)
- Optional premium services:
  - Hosted documentation hosting
  - Private kit registry (enterprise)
  - Analytics and kit performance metrics
  - Training programs for kit creators
  - Commercial support

**Rationale**: Sustainability requires clear governance and revenue models. Being explicit about incentives prevents resentment and ensures long-term commitment.

---

## Success Metrics (PMF for the Platform)

### For Kit Users

**Primary Metrics**:
- **Adoption**: 1,000+ downloads per month by month 6
- **Retention**: 70%+ of users return within 30 days
- **Willingness to Pay**: 20%+ of users upgrade to premium services within 12 months
- **Community Growth**: Active discussions on 20+ published kits
- **Time-to-First-Value**: 50%+ of users report actionable insights within first project (typically 2-4 weeks)

### For Kit Publishers

**Primary Metrics**:
- **Publisher Satisfaction**: 4.0+/5.0 rating on "ease of publishing"
- **Publisher Retention**: 80%+ of publishers maintain their kit for 12+ months
- **Innovation**: 5+ new kit variants published per quarter
- **Revenue**: 30% of publishers generate sustainable income (>$1k/month) from kits by month 18

### For Platform

**Primary Metrics**:
- **Total Downloads**: 100,000+ by month 12
- **Published Kits**: 50+ kits with active development
- **Community Size**: 10,000+ registered users
- **Accessibility**: Kits available in 3+ languages
- **Sustainability**: Platform generates >$100k annual revenue enabling dedicated team

---

## Development Roadmap (PMF Discovery Phases)

### Phase 0: Foundation (Months 1-2)

**Goal**: Prove core value with early adopters

**Actions**:
- Launch MVP platform with 5-10 hand-selected kits (PMF-Kit, PD-Kit, etc.)
- Recruit 100 beta users (friends + initial community)
- Conduct 20 user interviews to understand discovery patterns
- Gather feedback on installation experience
- Measure time-to-first-value

**Success Criteria**:
- 70%+ of users successfully install a kit
- 50%+ complete first project using installed kit
- Net Promoter Score >30

### Phase 1: Publisher Enablement (Months 3-4)

**Goal**: Enable first external kit publishers

**Actions**:
- Publish kit creator guide
- Launch "Create Kit" wizard
- Recruit 3-5 external publishers
- Provide direct support to first publishers
- Gather feedback on publishing workflow

**Success Criteria**:
- 5+ kits published by external creators
- Publisher satisfaction >4.0/5.0
- Template validation 100% automated

### Phase 2: Community & Curation (Months 5-6)

**Goal**: Build community momentum and implement curation

**Actions**:
- Launch featured collections
- Host first community showcase
- Implement user reviews and ratings
- Start kit performance metrics
- Begin user interviews with 20+ practitioners

**Success Criteria**:
- 50+ published kits
- 10,000+ downloads
- Top kits averaging 4.2/5.0 stars
- 100+ kit reviews published

### Phase 3: Monetization (Months 7-9)

**Goal**: Develop sustainable revenue model

**Actions**:
- Launch premium features (hosted docs, analytics)
- Offer grants to top publishers
- Implement support tier system
- Partner with 5 organizations for sponsorships
- Conduct pricing research

**Success Criteria**:
- 100+ premium subscribers
- $20k MRR from platform revenue
- 30% of publishers generating income from kits

### Phase 4: Scale (Months 10-12)

**Goal**: Expand globally and vertically

**Actions**:
- Localize platform (3 languages)
- Launch enterprise private registry
- Expand to 5 new industry verticals
- Hire dedicated platform team
- Publish annual state-of-the-state report

**Success Criteria**:
- 100,000+ downloads
- 50+ published kits
- 10,000+ registered users
- $100k+ annual revenue
- Industry recognition (featured in 5+ major publications)

---

## Quality Standards

### Kit Acceptance Criteria

Every published kit MUST include:

1. **Constitution.md** (100% required)
   - Clear principles adapted to domain
   - Governance and amendment procedures
   - Multi-agent compatibility requirements
   - Success metrics specific to domain

2. **Templates** (100% required)
   - `spec-template.md` (tailored to domain)
   - `plan-template.md` (execution roadmap)
   - `tasks-template.md` (actionable tasks)
   - At least 3 example use-cases

3. **Documentation** (100% required)
   - Quick-start guide (<10 min to first result)
   - Full reference documentation
   - FAQ addressing common challenges
   - Video walkthrough (strongly preferred)

4. **Examples** (100% required)
   - Completed spec.md example
   - Completed plan.md example
   - Completed tasks.md example
   - Real or realistic scenario (not invented)

5. **Registry Metadata** (100% required)
   - Kit name (unique in namespace)
   - Version following semantic versioning
   - Publisher name and contact
   - License (MIT, Apache 2.0, or equivalent)
   - 1-2 sentence description
   - 5 relevant tags for discovery

6. **Validation** (100% required)
   - All templates pass automated linting
   - Multi-agent compatibility verified (≥2 agents)
   - Documentation is current and accurate
   - Examples use realistic data

---

## Kit Namespace Registry

### Reserved Namespaces

```
/pmfkit.*                    # PMF-Kit (core, reserved)
/speckit.*                   # Spec-Kit (upstream, reserved)
/agentiikits.*               # Agentii-Kit marketplace commands
```

### Published Kit Namespaces

```
/marketing-kit.*             # Marketing operations workflows
/pd-kit.*                    # Product design workflows
/legal-kit.*                 # Legal operations workflows
/sales-kit.*                 # Sales enablement workflows
/hr-kit.*                    # Human resources workflows
/<your-org>-kit.*            # Custom organizational kits
```

### Namespace Request Process

1. Submit namespace request to registry@agentii.ai
2. Include: Organization name, kit name, use case
3. Verify no conflicts with existing kits
4. Publish namespace reservation in registry
5. Kit must be published within 6 months or namespace released

---

## Non-Goals (What Agentii-Kit Will NOT Do)

- **Replace version control systems** (GitHub, GitLab remain sources of truth)
- **Enforce particular methodologies** (multiple approaches coexist)
- **Require proprietary tools** (works with open-source + popular platforms)
- **Collect user research data** (each kit publisher owns their data)
- **Provide customer support for installed kits** (publishers are responsible)
- **Take equity in or control kit publishers** (publishers remain independent)
- **Centralize all knowledge work** (kits are starting points, not endpoints)

---

## Constitutional Amendments

### Amendment Procedure

1. Propose changes via RFC (Request for Comments)
2. Discuss with Kit Publisher Advisory (30 days minimum)
3. Hold public comment period (14 days)
4. Vote with 2/3+ majority from Advisory + Founder Sign-off
5. Update version and document rationale
6. Notify all active kit publishers

### Versioning Policy

- **MAJOR (X.0.0)**: Changes affecting kit compatibility or governance
- **MINOR (0.X.0)**: New features or expanded kit requirements
- **PATCH (0.0.X)**: Clarifications or non-breaking refinements

### Next Amendment Cycle

Planned for 2026-Q2 (annual review)

---

## Assumptions & Risks

### Key Assumptions

1. **Market Demand**: Practitioners across domains want structured, reusable methodologies
2. **Publisher Interest**: Experts in other domains will create and maintain kits
3. **Platform Sustainability**: Revenue model (premium services) can sustain platform development
4. **Community Engagement**: Users will participate in curation and reviews

### Risk Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|-----------|
| Low adoption from users | Platform fails | Medium | Invest in discovery UX and community building |
| Few external publishers | Limited kit variety | Medium | Invest in creator enablement, offer grants |
| Competing platforms emerge | Market fragmentation | High | Build strong community network effects |
| Platforms become unmaintained | Degraded experience | Medium | Establish publisher SLAs and take over inactive kits |
| Security or privacy breach | Loss of trust | Low | Security-first architecture, regular audits |

---

## Governance Schedule

- **Weekly**: Core team syncs on platform development
- **Bi-weekly**: Kit Publisher Advisory meetings
- **Monthly**: Community forum discussion threads
- **Quarterly**: Public roadmap updates and RFC cycles
- **Annually**: Community conference + governance review

---

## Conclusion

Agentii-Kit succeeds by making exceptional methodologies accessible, enabling specialists to grow their domains, and building a thriving ecosystem of creators and users. This constitution codifies the principles enabling that vision.

**Ratified by**: Frank Chen, Founder & CEO, Agentii
**Date**: 2025-12-05
**Status**: Draft (Community Feedback Welcome)

