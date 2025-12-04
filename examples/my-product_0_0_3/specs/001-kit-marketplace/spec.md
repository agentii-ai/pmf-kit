# agentii-kit Marketplace Specification

**Feature Branch**: `001-kit-marketplace`
**Created**: 2025-12-04
**Status**: Draft
**Discovery Focus**: Open-source marketplace platform for spec-kit job kit variants

## Overview

**What we believe**: Spec-Driven Development (SDD) is a domain-agnostic methodology that transforms any knowledge work into structured, AI-agent-executable workflows. By building an open-source marketplace where domain experts can publish, discover, and fork specialized "job kits," we can unlock professional productivity across marketing, legal, product, finance, education, and beyond—just as GitHub revolutionized code collaboration.

**Who we're solving for**: Domain experts, subject matter authorities, and professional practitioners who want to codify their expertise into reusable, AI-agent-ready workflows that their peers and teams can fork, customize, and execute.

**Why now**: (1) AI agents like Claude Code and Cursor have proven the ability to execute structured workflows at scale; (2) GitHub's `.cursorrules` and Fabric's pattern libraries show demand for standardized, shareable expertise; (3) the "kit economy" is emerging—users want pre-built, vetted solutions, not blank canvases.

---

## Personas & Segments *(mandatory)*

### Primary Persona: Domain Expert Kit Creator

**Context**:
- **Role**: Product Manager, Legal Counsel, Marketing Director, Financial Analyst, or Educational Specialist with 5+ years domain experience
- **Company**: Startups to mid-market (10–500 people); some independent consultants
- **Team**: Often solo or small team; may collaborate with peers in their field
- **Tools they use**: GitHub, Claude Code / Cursor, Notion, Slack; familiar with version control
- **Success metric**: Their kit is downloaded/forked 100+ times in first 6 months; community contributes improvements; credited as an expert

**Pain Profile**:
- **Top pain**: Their hard-won domain knowledge (frameworks, templates, checklists) lives in personal Notion/Confluence; impossible to share at scale or benefit from peer contributions
- **Current workaround**: Email templates, Gumroad PDFs, private GitHub repos, closed Slack communities—all have poor discoverability and no forking/versioning
- **Willingness to try**: High—they want to be recognized as experts; prefer open-source contribution over selling templates; excited by possibility of community improvements

### Secondary Persona: Professional Practitioner Kit User

**Context**:
- **Role**: Junior PM, Paralegal, Content Marketer, Accountant, High School Teacher
- **Company**: Any size; mostly employed (some freelance)
- **Tools**: Same as above; GitHub-literate or willing to learn
- **Success metric**: Save 10+ hours/month on routine tasks; output quality improves; can run workflows independently

**Pain Profile**:
- **Top pain**: Repeating the same processes every project (job applications, contract reviews, content briefs, lesson planning); inconsistent quality; no leverage from peer expertise
- **Current workaround**: Cobbling together templates from Slack, PDFs, memories of past projects; asking senior colleague for their template (inconsistent)
- **Willingness to try**: High—they value time saved and quality improvement; will fork and customize kits if they're easy to use

### Segment You're NOT Building For

- **Enterprise IT teams** (too rigid, require procurement): Addressed in Phase 2 with enterprise deployment options
- **Non-technical professionals without GitHub access** (excluded initially): Phase 2 includes low-code discovery UI
- **Code-only developers** (excluded): agentii-kit complements spec-kit; developers use spec-kit; professionals use agentii-kit job kits

---

## Problems & Jobs-to-Be-Done (JTBD) *(mandatory)*

### Primary JTBD #1: Codify & Share Domain Expertise (Priority: P1)

**Job Story**: When I realize my team (or professional community) repeats the same processes every project, I want to codify my best practices and workflows into reusable templates, so I can ensure consistency, multiply my impact, and become recognized as the expert.

**Current Workaround**: Create private Notion databases, email templates as PDFs, or write Medium essays describing processes; share ad-hoc in Slack or email

**Frequency**: Quarterly to annually (evergreen; done once per process)

**Evidence of willingness-to-pay**: Experts publish free on Medium and Twitter; GitHub stars on template repos; excitement about "creating frameworks"; willingness to contribute to Fabric, ORCA, and similar communities

**Success signal**: "My kit has 50+ stars and forks; people I don't know are using it and suggesting improvements"

### Primary JTBD #2: Discover & Adopt Expert Workflows (Priority: P1)

**Job Story**: When starting a new project or joining a new domain, I want to find vetted, expert-designed workflows that solve my problem, so I can execute at high quality from day one without reinventing the wheel or asking for help.

**Current Workaround**: Google "best practices for [task]," ask colleagues, scroll Product Hunt or Hacker News, hope someone shared a GitHub repo

**Frequency**: Monthly to quarterly (starting new projects, switching roles)

**Evidence of willingness-to-pay**: High engagement with Product Hunt launches; trending repos; retweets of "how-to" threads; demand for Notion template marketplaces

**Success signal**: "I forked this Legal-Kit and in 30 minutes had a first draft of my NDA redline"

### Primary JTBD #3: Customize & Iterate on Workflows (Priority: P2)

**Job Story**: When I fork an expert kit, I want to easily adapt it to my context (company, jurisdiction, team size), so I can use proven workflows while maintaining my unique requirements and contributing improvements back.

**Current Workaround**: Copy-paste PDF into Google Docs, manually edit everything, lose connection to original; no way to track updates or contribute fixes back

**Frequency**: Once per kit adoption (usually 1-2 per quarter per professional)

**Evidence of willingness-to-pay**: GitHub forks and pull requests; community engagement in open-source; frustration with template marketplaces that don't allow modification

**Success signal**: "I customized the SEO-Kit for my niche, and when I found a bug, I submitted a pull request that got merged"

---

## Hero Workflows *(mandatory)*

### Hero Workflow 1: Kit Creator - "Publish a Domain-Expert Kit"

**Why this workflow matters**: Enables recognized experts to immediately have impact; creates flywheel where great kits attract users, users contribute improvements, and kit becomes standard in the field.

**End-to-end flow**:

1. **Input**: Domain expert has a process or framework they want to share (e.g., Marketing Director with a launch checklist)
2. **Process**:
   - Browse agentii-kit homepage and find "Create Kit" button
   - Fork a kit template or start from scratch (defaults to minimal structure)
   - Define their kit's constitution.md (5–7 core principles for their domain)
   - Create spec-template.md (what domain practitioners need to specify)
   - Create plan-template.md (how to execute domain work)
   - Add 1–2 worked examples (walkthrough of hero workflow)
   - Write README and publish to agentii-kit registry
3. **Output**: Published kit at `agentii.ai/kits/[domain]-kit`; available for forking; appears in marketplace discovery
4. **Success signal**: Kit appears in search results; other experts see it and cite it

**TTFW (Time-to-First-Workflow) Target**: < 30 minutes to publish a basic kit

**Guardrails & Error Recovery**:
- What breaks: Expert tries to publish without examples; kit has missing required sections (constitution.md)
- How users recover: CLI/UI validation runs before publishing; provides checklist of missing items; suggests templates
- Backstop: Kit review queue; platform maintainers can request changes before publication

### Hero Workflow 2: Kit User - "Fork, Customize, Execute a Kit"

**Why this workflow matters**: Demonstrates core value—users can achieve professional goals faster using vetted workflows; builds retention and community

**End-to-end flow**:

1. **Input**: Professional needs to execute a task (e.g., Junior PM launching a feature; needs process)
2. **Process**:
   - Search agentii-kit for "product launch" or browse "PM Kits"
   - Find "Product Launch Kit" (highly rated, has 500+ forks)
   - Click "Fork This Kit" → creates copy in their GitHub or agentii workspace
   - Customize spec.md with their product details (name, target audience, launch date)
   - Run through constitution, spec, plan, tasks workflow using their AI agent (Claude Code, Cursor, etc.)
   - Execute tasks and generate launch artifacts (messaging, timeline, GTM strategy)
3. **Output**: Completed launch plan tailored to their product
4. **Success signal**: "I completed my launch plan in 4 hours instead of 2 weeks; my team loved the process"

**TTFW Target**: < 15 minutes from discovering kit to executing first task in agent

**Guardrails & Error Recovery**:
- What breaks: User's AI agent doesn't support the kit's slash commands; required data is unclear
- How users recover: Kit includes agent compatibility matrix; clear examples with sample data; troubleshooting guide
- Backstop: User can ask questions on kit's GitHub Discussion; community and maintainer answer

---

## Success Metrics & PMF Signals *(mandatory)*

### Activation Metrics (Kit Creator)

- % of kit creators who publish at least one complete kit within first month
- % of kit creators who rate their experience >= 4/5 for ease of publication

### Activation Metrics (Kit User)

- % of users who fork at least one kit within first session
- % of users who customize and execute kit tasks with their AI agent

### Engagement Metrics (Kit Creator)

- % of kits that receive >= 1 pull request or GitHub Discussion in first 6 months
- Frequency: PRs / forks per kit per month

### Engagement Metrics (Kit User)

- Frequency: kits executed per active user per month
- Depth: % of users who fork > 1 kit over 3 months

### Retention Metrics

- Day-7 / Day-30 retention of kit creators
- Day-7 / Day-30 retention of kit users
- Churn: % of kits that go unmaintained (no updates in 6 months)

### Community Metrics

- Number of unique kit domains launched (PM, Legal, Marketing, Finance, HR, Education, etc.)
- GitHub stars on agentii-kit platform repo
- % of new kits authored by community (vs. official platform)

### AI-Specific Metrics

- % of kit users who rate kit's AI-generated outputs as "helpful" (4-5 scale)
- % of kit templates successfully executed without errors on first run
- Multi-agent coverage: % of kits that work with Claude Code, Cursor, Copilot, Gemini

### Business Metrics

- Marketplace reach: unique kit downloads per month
- Virality: forks / original kit usage ratio
- Quality: average rating of published kits (community rating 1-5)

### PMF Validation Threshold

- Kit creator PMF: 50+ creators publish at least 1 kit; 40%+ report "I couldn't use any other tool for this"
- Kit user PMF: 1000+ users complete hero workflow; 40%+ report "this saved me 10+ hours"
- Community health: 20+ kit domains with >= 3 kits each; active cross-kit collaboration

---

## Constraints & Risks *(mandatory)*

### Technical Feasibility

- Multi-agent compatibility: Kits must execute correctly on Claude Code, Cursor, GitHub Copilot, Gemini Code; initial MVP supports 2 agents
- Discoverability performance: Kit search results must return in < 1 second for 10K+ published kits
- Fork / customization mechanics: Users must be able to fork and customize kits in < 5 clicks; no git CLI required for MVP
- Specification clarity: Kit templates must be parseable by AI agents without errors on 95%+ of first runs

### Competitive Landscape

- **Direct competitors**: Notion template marketplace (limited collaboration), Gumroad (poor discoverability), Zapier Blueprints (limited to automation), Fabric patterns (task-oriented, not project-oriented)
- **Why we're different**: (1) Git-based collaboration mirrors GitHub's success; (2) Spec-Driven Development brings structure lacking in other marketplaces; (3) Multi-kit interoperability; (4) Free, open-source, no vendor lock-in
- **Incumbent workaround**: Professionals use Google Drive, Notion, Asana templates, internal wikis; discovery via word-of-mouth, Twitter, Reddit

### Top 3 PMF Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **Kit quality inconsistent**: Many published kits are low-quality, incomplete, or not useful; users waste time on bad templates | High | Pre-publication curation: validation checklist, 2-person review before "featured" status; rating/feedback system; flag low-quality kits; highlight top-rated kits in discovery |
| **Adoption friction**: Users don't understand how to fork, customize, or execute kits; AI agent compatibility issues frustrate adopters | High | Create video tutorials (< 2 min) for hero workflows; provide sample kits pre-loaded with real examples; offer office hours Q&A; document all agent compatibility issues; one-click fork with templates |
| **Cold start**: Few creators publish in first month; few users discover value without large catalog | Medium | Seed with 5-7 high-quality official kits (PM-Kit, Marketing-Kit, Legal-Kit, SEO-Kit, Founder-Kit, Edu-Kit, Finance-Kit); partner with 2-3 domain experts to publish on day 1; heavy social media seeding; Product Hunt launch with category |

---

## Distribution & Adoption Hypotheses *(mandatory)*

### Primary Channel Hypothesis

- **Channel**: Product Hunt + GitHub trending (launch with 5 official kits to "own" the category)
- **Rationale**: Early adopters in SDD space are already on PH; GitHub audience includes domain experts and practitioners; PH launch signals legitimacy
- **Success criterion**: 300+ upvotes on Product Hunt; 2K+ GitHub stars in first week; 100+ kit forks in first month

### Secondary Channels (Ordered by Priority)

1. **Twitter/X**: Problem-solution storytelling about domain expertise codification; retweet by spec-kit creators; creator interviews
2. **Communities** (Reddit, Discord): r/productivity, r/startups, r/marketing, r/law, r/teachers; direct engagement in existing threads; offer to create kits for their pain points
3. **Content**: "Why we built agentii-kit" blog; technical deep-dive on spec-driven methodology for non-coders; case studies from early creators
4. **Partnerships**: Outreach to Cursor, Claude Code teams; ask for promotion in agent docs/communities; work with spec-kit maintainers on cross-promotion

### Viral/Network Hypothesis

- **Does collaboration/sharing drive value?** YES—heavily. Users share kits with teammates; teams that adopt a kit create shared workflows; network effects compound.
- **Mechanism**: User forks PM-Kit → shares with team in Slack → team members all fork and execute → team becomes the "standard" in their company → they contribute improvements back → kit evolves

### Early Adopter Profile

- **Who jumps at this first?** Product managers and founders familiar with spec-kit; marketers frustrated with template fragmentation; legal professionals wanting to systematize workflows
- **Where to find them?** GitHub spec-kit community; Cursor and Claude Code forums; Twitter threads on productivity/frameworks; YC startup community; Product Hunt early adopters
- **How to activate them?** Private beta access 1 month before public launch; direct outreach for kit creation partnerships; highlight their kits publicly on launch day

---

## Success Criteria for Discovery Phase *(mandatory)*

Before proceeding to research planning, we consider discovery successful when:

- [ ] **Creator Persona Validation**: Conducted 5-10 interviews with domain experts (PM, Legal, Marketing); personas feel distinct and real
- [ ] **User Persona Validation**: Conducted 5-10 interviews with junior practitioners; strong signals of problem urgency and willingness to adopt
- [ ] **JTBD Clarity**: All 3 primary JTBDs consistently mentioned across interviews; evidence of willingness-to-pay evident
- [ ] **Hero Workflow Buy-In**: 3-5 domain experts manually created/published a kit; 5-10 practitioners forked and executed kits end-to-end; "wow moments" observed
- [ ] **Multi-kit Interoperability**: Confirmed that users can run kits across Claude Code, Cursor; minor agent-specific issues are handleable
- [ ] **Metrics Feasibility**: Confirmed that GitHub API, web analytics, and survey tools can instrument all success metrics
- [ ] **Risk Acknowledgment**: Top 3 risks explicitly stated; mitigation plans drafted and assignable to launch team
- [ ] **Go-to-Market Confidence**: Product Hunt, GitHub, Twitter distribution plans finalized; creator partnerships confirmed for day-1 launch

---

## Open Questions

- **Kit quality gate**: Should we require peer review / voting before a kit becomes "featured," or publish all kits and let community ratings drive discovery? [NEEDS CLARIFICATION: impacts curation burden and early-stage volume]
- **Monetization**: Should agentii-kit remain 100% free/open, or introduce premium features (private kits, private registry, early access to new features)? [NEEDS CLARIFICATION: impacts sustainability and business model alignment]
- **AI agent support priority**: Should we support all major agents (Claude, Cursor, Copilot, Gemini, etc.) from day 1, or start with 1-2 and expand? [NEEDS CLARIFICATION: affects launch scope and testing burden]

---

## Assumptions

- **GitHub will remain free/open**: Core assumptions depend on GitHub's continued support for public repos, forks, and collaboration
- **AI agent slash-command adoption continues**: Kits depend on agents supporting structured file-based workflows; assumes this remains the case
- **Domain experts want visibility**: Assumes creators are motivated by recognition and impact, not primarily by revenue; we may need to introduce monetization later
- **Practitioners are GitHub-literate or willing to learn**: MVP assumes basic comfort with repos/forks; Phase 2 will add UI for non-technical users

---

## AI Product References

**Products with similar hero workflows** (for pattern reference):

- **GitHub**: Repo discovery → fork/clone → customize → contribute back → reputation/influence. Similar network effects apply to kits.
- **Cursor**: Detected unmet need (faster coding); made onboarding < 5 min; early adopter community drove viral adoption; now 50K+ users in 6 months
- **Notion template marketplace**: Solved "blank page" problem; discovered high demand for pre-built templates; limited by poor collaboration/forking

**Key PMF patterns we're following**:

- **Network effects**: Early creators attract users; users attract creators; flywheel compounded by GitHub's built-in collaboration
- **Community validation**: Public ratings, reviews, and contributions build trust; open-source model attracts expert creators
- **Low TTFW**: Discoverability and fork mechanics must be < 2 minutes to reduce friction
- **Domain specialization**: Instead of generic templates, obsess over 1-2 domains first (PM, Marketing) to build depth and credibility

---

## Next Steps

**Immediate**: Run `/pmfkit.clarify` to resolve the 3 open questions above

**If clarification passes**: Run `/pmfkit.plan` to design discovery research methodology and launch go-to-market strategy

**If risks are high**: Conduct founder interviews with 5-10 domain experts to validate kit creation flow and perception of platform value
