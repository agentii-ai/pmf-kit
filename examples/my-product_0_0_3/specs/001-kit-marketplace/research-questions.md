# Phase 0: Research Questions & Hypothesis Clarification

**Feature**: agentii-kit marketplace platform
**Branch**: `001-kit-marketplace`
**Created**: 2025-12-04
**Purpose**: Operationalize all spec-derived hypotheses into testable research questions with clear success criteria

---

## Hypothesis Framework

All hypotheses are derived from and traceable to spec.md assertions. Research is organized into 5 hypothesis clusters:

1. **Creator JTBD Validation**: Domain experts genuinely need to codify and share expertise
2. **User JTBD Validation**: Practitioners genuinely need discovery and adoption of expert workflows
3. **Hero Workflow Feasibility**: Both hero workflows are achievable in target time frames
4. **Market Readiness**: Market signals support demand for a kit marketplace
5. **Distribution Effectiveness**: Primary channel (Product Hunt + GitHub) can drive early adoption

---

## Hypothesis Cluster 1: Creator JTBD Validation

### H1.1: Domain Experts Feel Acute Pain Sharing Knowledge

**JTBD**: "Codify & Share Domain Expertise" (spec.md, P1)

**Hypothesis**: Domain experts (PM, Legal, Marketing, Finance, Education specialists with 5+ years) experience repeated pain when trying to share domain knowledge at scale; current workarounds (Notion, Gumroad, email) are inadequate.

**Research Question**: Do target domain experts report high-frequency pain (weekly/monthly) with current knowledge-sharing workflows?

**Methodology**:
- In-depth interviews: N=12-15 domain experts (2-3 per domain: PM, Legal, Marketing, Finance, Education)
- Duration: 60 min per interview
- Channels: LinkedIn outreach, domain-specific communities (r/legal, ProductTank forums, marketing Slack communities)
- Interview focus: Current knowledge-sharing challenges, frequency of pain, workarounds, time spent

**Success Criteria** (Go/No-Go threshold):
- **GO**: 70%+ of interviewed experts report pain with current workflows; 80%+ report monthly+ frequency; 75%+ mention "want recognition" or "want to help community"
- **NO-GO**: <50% report pain; <50% have tried sharing with others
- **PIVOT**: Pain exists but is asymmetric (e.g., only legal experts, not others)

**Sample Validation Questions**:
- "Walk me through the last time you tried to share a process or framework with others. What went well? What was frustrating?"
- "How often do you attempt to codify and share domain knowledge? What prevents you from doing it more?"
- "If you could design the ideal way to share your expertise, what would that look like?"

---

### H1.2: Creators Are Motivated by Recognition, Not Revenue

**JTBD**: Codify & Share Domain Expertise (spec assumption: creators want visibility, not monetization initially)

**Hypothesis**: Domain experts are primarily motivated by recognition, impact, and community contribution; they prefer open-source contribution over selling templates; they would willingly publish for free if their kit gets visibility and community engagement.

**Research Question**: What motivates domain experts to create and share knowledge products? (Revenue vs. recognition vs. impact)

**Methodology**:
- In-depth interviews: Same N=12-15 as H1.1 (integrated into same conversation)
- Contextual evidence: GitHub repository analysis (N=20-30 popular open-source template/kit repos) - star patterns, contributor engagement, creator background
- Comparison: Survey N=30 creators who published on Gumroad vs. GitHub to compare monetization attempts

**Success Criteria**:
- **GO**: 80%+ of experts express strong preference for open-source/free publication if visibility is high; 70%+ mention "recognition" or "helping others" as primary motivator
- **NO-GO**: >50% prioritize revenue; <30% interested in open-source approach
- **PIVOT**: Bimodal motivation (e.g., some want revenue, some want recognition) → segment strategy needed

---

### H1.3: Kit Publication Flow is Achievable in <30 Minutes

**Hero Workflow 1**: Kit Creator - "Publish a Domain-Expert Kit" (spec.md TTFW target: <30 min)

**Hypothesis**: Domain experts can publish a basic, complete kit (with constitution, templates, and 1-2 examples) in under 30 minutes with provided templates and clear guidance.

**Research Question**: Can domain experts successfully create and publish a kit in <30 minutes with current scaffolding?

**Methodology**:
- Moderated usability testing: N=5-8 domain experts
- Protocol: Provide kit template scaffold, brief onboarding, ask them to "create a basic kit for your domain in 30 min"
- Measurement: Time to completion, errors/confusion, satisfaction rating (1-5), whether output is "publishable"
- Observation: Where do they get stuck? What's unclear? What's easy?

**Success Criteria**:
- **GO**: 70%+ complete in <30 min; average satisfaction >=4/5; output is quality (constitution defined, templates filled, example included)
- **NO-GO**: <50% complete in <30 min; average satisfaction <3/5; majority of outputs are incomplete
- **PIVOT**: 50-70% complete in time, but require 2-5 min onboarding → design better UX/docs

---

## Hypothesis Cluster 2: User JTBD Validation

### H2.1: Practitioners Feel Pain Finding & Adopting Expert Workflows

**JTBD**: "Discover & Adopt Expert Workflows" (spec.md, P1)

**Hypothesis**: Junior PMs, paralegals, marketers, accountants, and teachers regularly experience pain when trying to find and apply expert workflows; they currently waste 5-20 hours per project on repeated processes.

**Research Question**: Do target practitioners report high-frequency pain (monthly+) with current process discovery and execution?

**Methodology**:
- In-depth interviews: N=12-15 practitioners (2-3 per role: Junior PM, Paralegal, Content Marketer, Accountant, Teacher)
- Duration: 45 min per interview
- Channels: LinkedIn, community forums (r/productivity, legal subreddits, marketing communities), career groups
- Interview focus: Current workflow discovery process, time spent, pain points, frequency of repeating processes

**Success Criteria**:
- **GO**: 75%+ report monthly+ pain; 70%+ estimate 5+ hours lost per project on repetition; 80%+ currently use workarounds (templates from colleagues, past projects, PDFs)
- **NO-GO**: <50% experience pain; <40% report significant time loss
- **PIVOT**: Pain is role-specific (e.g., only paralegals, not accountants) → focus on high-pain segments first

---

### H2.2: Practitioners Value Time Savings & Quality Improvement

**JTBD**: Discover & Adopt Expert Workflows (success signal: "saved me 10+ hours")

**Hypothesis**: Practitioners would adopt expert kits if they provide measurable value: 50%+ reduction in project time; 40%+ improvement in work quality; ability to execute independently without asking for help.

**Research Question**: What would motivate practitioners to fork and use an expert kit? What's their willingness to pay (free vs. freemium)?

**Methodology**:
- In-depth interviews: Same N=12-15 as H2.1
- Conjoint analysis (optional): Pricing & feature trade-off survey (N=50-100 practitioners) if needed
- Contextual: Monitor Notion template marketplace, Gumroad trends to understand existing demand/pricing

**Success Criteria**:
- **GO**: 80%+ of practitioners report they would "definitely" or "very likely" use a kit that saves 5+ hours; 70%+ prefer free with option to contribute; willingness to pay ranges from $0-$20/month
- **NO-GO**: <50% interested; <30% willing to try even if free
- **PIVOT**: Practitioners only interested if specific domain-focused (e.g., only PMs interested in Product-Kit, not Finance-Kit)

---

### H2.3: Kit User Hero Workflow is Achievable in <15 Minutes

**Hero Workflow 2**: Kit User - "Fork, Customize, Execute a Kit" (spec.md TTFW target: <15 min)

**Hypothesis**: Practitioners can discover a relevant kit, fork it, customize spec.md with their context, and begin executing tasks with their AI agent in under 15 minutes.

**Research Question**: Can practitioners successfully go from "kit discovery" to "first task execution" in <15 minutes?

**Methodology**:
- Moderated usability testing: N=8-10 practitioners (mix of roles)
- Protocol: Give them problem statement (e.g., "You're launching a product next month and need a launch plan"); have them find PM-Kit, fork, customize, and execute first task with Claude Code/Cursor
- Measurement: Time to completion, errors/confusion, satisfaction, whether they successfully generated useful output
- Observation: Where do discovery, forking, customization, or agent integration break down?

**Success Criteria**:
- **GO**: 75%+ complete flow in <15 min; 70%+ generate useful first output; average satisfaction >= 4/5
- **NO-GO**: <50% complete in <15 min; <60% produce useful output
- **PIVOT**: Can fork/customize in time but agent integration takes longer → improve agent docs/compatibility

---

## Hypothesis Cluster 3: Market Signals

### H3.1: Demand for Template Marketplaces is Real

**Market Signal**: Notion template marketplace, Gumroad success, Fabric contributions

**Hypothesis**: There is existing demand for expert-designed templates/kits; this demand can be redirected to agentii-kit if we solve discoverability and collaboration better than incumbents.

**Research Question**: How many professionals are currently buying/using templates? What do they complain about? Why might they switch to open-source?

**Methodology**:
- Quantitative: Survey existing template users (N=100-200) on Notion marketplace, Gumroad, Zapier communities
  - Questions: Where do they find templates? What's missing? Would they use open-source?
- Contextual: Analyze GitHub trending template repos (N=20-30) - track stars, forks, contributor diversity over time
- Competitive: Map Notion marketplace, Gumroad, Zapier competitors - identify gaps

**Success Criteria**:
- **GO**: >60% of template users report "discoverability is hard" or "can't collaborate with creators"; >70% interested in open-source alternative if better quality/discovery
- **NO-GO**: <40% interested in switching; template market showing decline
- **PIVOT**: Market prefers specific domain (e.g., high demand in Legal but not Marketing) → focus there first

---

### H3.2: AI Agent Adoption is at Inflection Point

**Market Signal**: Claude Code, Cursor adoption accelerating; `.cursorrules` trend; Fabric engagement

**Hypothesis**: AI agents (Claude Code, Cursor, Copilot, Gemini) are crossing adoption threshold where structured workflows are normal; this timing is optimal for kit marketplaces.

**Research Question**: Are domain professionals actively using AI agents and open to agent-based workflows?

**Methodology**:
- In-depth interviews: Add to creator/practitioner interviews (H1.1, H2.1) - "Are you using Claude Code or Cursor? How would you feel about workflows that integrate with them?"
- Contextual: GitHub stars/trends on claude-code, cursor repos; Reddit/Twitter sentiment on agent adoption in non-dev fields
- Competitive: Examine Fabric adoption metrics, `.cursorrules` GitHub prevalence

**Success Criteria**:
- **GO**: 60%+ of practitioners have tried Claude Code or Cursor; 70%+ comfortable with agent-based workflows; 80%+ willing to use kits that integrate with agents
- **NO-GO**: <40% familiar with agents; <50% open to them
- **PIVOT**: Adoption concentrated in certain roles/companies → target high-adoption segments first

---

## Hypothesis Cluster 4: Hero Workflow Integration

### H4.1: Multi-Agent Compatibility is Technically Feasible

**Platform Constraint**: Spec.md requires kits work across Claude Code, Cursor, Copilot, Gemini

**Hypothesis**: Kits can be designed in a way that's compatible with all major AI agents without agent-specific forks; slash commands and file-based workflows translate across agents seamlessly.

**Research Question**: Can the same kit repository execute successfully on 2+ AI agents without modification?

**Methodology**:
- Technical testing: Create 2 reference kits (PM-Kit, Marketing-Kit); test full hero workflow (fork → customize → execute) on:
  - Claude Code
  - Cursor
  - GitHub Copilot (if slash command support)
- Measurement: Success rate, errors encountered, compatibility issues, time to fix per agent
- Scope: Test with N=5-10 real users per agent (not just internal testing)

**Success Criteria**:
- **GO**: 80%+ of kits work first-try on 2+ agents; <5% of issues require kit modification; most issues are agent-specific docs
- **NO-GO**: <60% cross-agent compatibility without major kit restructuring
- **PIVOT**: Focus on 1-2 agents initially (e.g., Claude Code + Cursor); other agents in Phase 2

---

## Hypothesis Cluster 5: Distribution & Go-To-Market

### H5.1: Product Hunt + GitHub Launch Can Drive Early Adoption

**Distribution Hypothesis** (spec.md, Primary Channel): Product Hunt + GitHub trending launch with 5 reference kits can achieve 300+ upvotes, 2K+ stars, 100+ forks in first month

**Hypothesis**: Early adopter community (spec-kit users, SDD enthusiasts, GitHub power users, Product Hunt regulars) will engage with agentii-kit launch if we pre-seed with high-quality reference kits and social validation.

**Research Question**: Will Product Hunt and GitHub audiences adopt agentii-kit? Which communities should we engage?

**Methodology**:
- Community outreach (Phase 0.5, exploratory):
  - Interviews with N=10-15 influencers/community leaders in:
    - spec-kit community (Reddit, Discord, GitHub discussions)
    - Cursor/Claude Code communities
    - Product Hunt early adopter groups
    - r/productivity, r/startups, r/marketing
  - Ask: Would you share this with your community? What would make it land better?
- Soft launch: Pre-release to N=50-100 beta testers from above communities; measure enthusiasm, content sharing
- Metric: Engagement rate (shares, discussions), quote requests, feedback quality

**Success Criteria**:
- **GO**: 70%+ of influencers willing to share; >80% of beta testers report "I'd recommend this to my community"; positive social sentiment on launch day predictive of PH performance
- **NO-GO**: <40% influencer interest; <50% beta tester enthusiasm
- **PIVOT**: Some communities enthused (e.g., spec-kit users) but not others (e.g., r/marketing) → phase launch by community

---

### H5.2: Early Adopter Profile Matches Spec Personas

**Hypothesis**: The earliest adopters (first 100-500 users) will be domain experts + junior practitioners who match our primary personas; they'll come from spec-kit, AI agent, and productivity communities—not from generic web.

**Research Question**: Who are the earliest adopters? Do they match our persona?

**Methodology**:
- Monitoring: Set up analytics on launch day to track:
  - Referral source (PH vs. GitHub vs. social media vs. communities)
  - User profile data (LinkedIn roles, GitHub history if available)
  - Behavior (which kits downloaded, which personas engaged)
- Surveys (post-launch): N=50-100 early adopters - "Where did you hear about agentii-kit? What's your role? Why interested?"

**Success Criteria**:
- **GO**: 60%+ of early adopters match our primary personas; 70%+ came from spec-kit/AI agent/productivity communities; cohort shows 30%+ D7 retention
- **NO-GO**: Adopters are generic/random; no persona clustering; low retention
- **PIVOT**: Adopter profile differs from persona (e.g., more engineers, fewer PMs) → adjust messaging or roadmap

---

## Research Execution Timeline (Phase 0 → Phase 1)

| Week | Milestone | Owner |
|------|-----------|-------|
| **Week 1 (Now)** | Finalize research instruments (interviews, usability test protocols); recruit participant pipeline | [Product Lead] |
| **Week 2** | Conduct creator interviews (H1.1, H1.2); conduct practitioner interviews (H2.1, H2.2) | [Research Lead] + [PMs] |
| **Week 3** | Hero workflow usability tests (H1.3, H2.3); analyze creator/practitioner feedback | [Design Lead] + [Product] |
| **Week 4** | Compile findings; create go/no-go decision matrix; present hypotheses status | [Product Lead] |

---

## Validation Checklist: Are All Hypotheses Linked to Spec?

- [x] H1.1-1.3 trace to Creator JTBD + Hero Workflow 1 in spec.md
- [x] H2.1-2.3 trace to User JTBD + Hero Workflow 2 in spec.md
- [x] H3.1-3.2 trace to market signals and competitive landscape in spec.md
- [x] H4.1 traces to technical constraints and multi-agent requirement in spec.md
- [x] H5.1-5.2 trace to distribution hypotheses and early adopter profile in spec.md

**Constitution Alignment**:
- [x] **Kit-First Specification** (Principle I): All research questions operationalize spec hypotheses
- [x] **Customer-Evidence-Driven** (Principle II, agentii adaptation): All questions require direct evidence (interviews, behavior, not assumptions)
- [x] **Iterative Validation** (Principle III): Research includes go/no-go checkpoints and pivot criteria
- [x] **Minimal Viable Process** (Principle IV): Qualitative interviews before surveys; sample sizes are lean (N=12-15 vs. N=1000)
- [x] **Multi-Kit Interoperability** (implied): H4.1 validates feasibility

---

## Next Steps

→ Proceed to `/pmfkit.plan` Phase 1 research instrument design to create:
- Interview protocols (research-instruments.md)
- Usability test scenarios
- Survey templates
- Participant recruitment criteria
- Validation checkpoints & go/no-go thresholds (validation-checkpoints.md)
