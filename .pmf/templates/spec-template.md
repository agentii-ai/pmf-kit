# PMF Specification: [PRODUCT NAME]

**Feature Branch**: `[###-pmf-discovery]`  
**Created**: [DATE]  
**Status**: Draft  
**Discovery Focus**: [AI Product Category]  
**Owner**: [Name/Role]

## Overview

**What we believe**: [Core hypothesis about market need - 1-2 sentences]

**Who we're solving for**: [Primary persona(s) - brief]

**Why now**: [Market signal or trigger - 1-2 sentences]

---

## Personas & Segments *(mandatory)*

<!--
  Focus on SHARP personas with role, company context, tools, and environment.
  Go deep on 1-2 primary personas; sketch secondary personas as needed.
  Include pain indicators and frequency of pain.
-->

### Primary Persona: [Persona 1 - Name & Role/Title]

**Context**:
- **Role**: [Specific title/function]
- **Company**: [Size, industry, stage] - e.g., "Senior PM at Series B SaaS (100-300 employees)"
- **Team**: [Who they collaborate with - e.g., "Works with 10-15 engineers, 2-3 designers"]
- **Tools they use**: [Current toolchain - e.g., "Notion, Figma, GitHub, Claude Code"]
- **Success metric**: [What success looks like - e.g., "Ship 3-5 features per quarter"]

**Pain Profile**:
- **Top pain**: [Verbatim quote format - e.g., '"Every new feature starts from a blank page. I waste 2-3 hours writing PRDs..."']
- **Pain frequency**: [Quantified - e.g., "2+ hours/week on workflow setup"]
- **Current workaround**: [How they solve it today - specific tools/processes]
- **Willingness to try**: [Signal with evidence - e.g., "Actively searches for 'PM templates' on Twitter/Reddit"]

### Secondary Persona: [Persona 2 - Role/Title]

[Same structure as above]

### Segment You're NOT Building For

[Explicitly state who you're excluding and why - e.g., "Enterprise IT teams" or "Individual hobbyists"]

---

## Problems & Jobs-to-Be-Done (JTBD) *(mandatory)*

<!--
  For each persona, identify the TOP 3 JTBD.
  Use job stories: "When [situation], I want to [action], so I can [outcome]"
  Include the current workaround and evidence of frequency/willingness-to-pay.
-->

### Primary JTBD #1: [Job Title] (Priority: P1)

**Job Story**: When [situation], I want to [action], so I can [outcome - functional/emotional/social]

**Current Workaround**: [What users do today - tool, manual process, etc.]

**Frequency**: [How often this job needs to happen - daily/weekly/monthly]

**Evidence of willingness-to-pay**: [Quantified signal with price anchors - e.g., "PromptBase users pay $3-10/prompt; Notion templates sell for $5-50"]

**Success signal**: [How users will know they've solved the job]

### Primary JTBD #2: [Job Title] (Priority: P2)

[Same structure]

### Primary JTBD #3: [Job Title] (Priority: P3)

[Same structure]

---

## Hero Workflows *(mandatory)*

<!--
  Define 1-2 hero workflows - the minimal end-to-end paths through your product
  that deliver the core value. Include TTFW target and guardrails.
-->

### Hero Workflow: [Workflow Name]

**Why this workflow matters**: [How it connects to top JTBD]

**End-to-end flow**:

1. **Input**: [What the user brings - data, context, problem]
2. **Process**: [Steps user takes - user-centric, not technical]
3. **Output**: [What they get - artifact, insight, decision]
4. **Success signal**: [Moment of obvious value - "wow, this saved me X"]

**TTFW (Time-to-First-Workflow) Target**: [e.g., "< 5 minutes for first productive use"]

**Guardrails & Error Recovery**:
- [What breaks the workflow?]
- [How do users recover?]
- [What's the backstop if AI fails?]

### Hero Workflow 2 (Optional): [If Multiple Entry Points Exist]

[Same structure as above]

---

## Success Metrics & PMF Signals *(mandatory)*

<!--
  Define how you'll know you're achieving PMF.
  Include activation, engagement, retention, and AI-specific metrics.
-->

### Activation Metrics

- [E.g., "≥15% of visitors complete hero workflow in first session"]
- [E.g., "≥60% create first artifact within 24 hours"]

### Engagement Metrics

- [E.g., "≥3 workflows per active user per week"]
- [E.g., "≥30% of users try 2+ features within 7 days"]

### Retention Metrics

- [E.g., "≥30% Day-7 retention of activated users"]
- [E.g., "≥20% Day-30 retention"]
- [E.g., "<5% monthly churn for activated cohort"]

### AI-Specific Metrics

- [E.g., "≥4.0/5.0 average quality rating for AI outputs"]
- [E.g., "≥70% of outputs used without modification"]
- [E.g., "≥80% user confidence in AI results (survey)"]
- [E.g., "≥95% cross-agent compatibility (Claude Code, Cursor, Copilot)"]

### Business Metrics

- [E.g., "≥40% indicate willingness to pay $5-20/mo in surveys"]
- [E.g., "LTV/CAC ratio ≥3:1 within 12 months"]
- [E.g., "Viral coefficient ≥0.3 (1 user → 0.3 new users)"]

### Marketplace Metrics (if applicable)

- [E.g., "Creator-to-user ratio: 1:10 to 1:20"]
- [E.g., "Cross-side conversion: ≥10% of users become creators within 30 days"]
- [E.g., "Network effects: R² > 0.4 correlation between supply growth and user signups"]

### PMF Validation Threshold

- [E.g., "Sean Ellis test: ≥40% would be 'very disappointed' without product"]
- [E.g., "Retention: ≥30% D30 for core segment"]
- [E.g., "NPS: ≥50 from activated users"]
- [E.g., "Creator satisfaction: ≥70% rate experience 4+ stars"]

---

## Constraints & Risks *(mandatory)*

### Technical Feasibility

- [E.g., "AI accuracy must be ≥85% for use case to be viable"]
- [E.g., "Latency requirement: <3 seconds for workflows to feel instant"]
- [E.g., "Data privacy: GDPR-compliant, no training on user data without consent"]

### Multi-Agent Compatibility

- **Target agents**: [E.g., "Claude Code (primary), Cursor (secondary), GitHub Copilot (stretch)"]
- **Compatibility threshold**: [E.g., "≥80% of workflows must work across 2+ agents without modification"]
- **Testing approach**: [E.g., "5 test runs per agent per hero workflow; document agent-specific workarounds"]

### Competitive Landscape

- **Direct competitors**: [List 3-5 products solving similar JTBD]
- **Why we're different**: [1-2 bullet contrasts]
- **Incumbent workaround**: [What users default to - spreadsheet, manual process, etc.]

### Top 3 PMF Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| [Risk 1 - e.g., "AI output quality insufficient"] | High | [Plan - e.g., "Conduct hero workflow tests with 10-20 users; measure satisfaction"] |
| [Risk 2 - e.g., "Personas don't perceive as differentiated"] | High | [Plan - e.g., "Interview 5 non-adopters to understand why"]  |
| [Risk 3 - e.g., "Distribution channel difficult/expensive"] | Medium | [Plan - e.g., "Test 3 channels (PH, Reddit, Twitter) with low budget first"] |

---

## Assumptions *(mandatory)*

<!--
  Document dependencies and beliefs that underpin this spec.
  Each assumption should have impact level and validation method.
-->

| Assumption | Impact if Invalid | Validation Method |
|------------|-------------------|-------------------|
| [E.g., "GitHub will remain free for public repos"] | High | [E.g., "Monitor GitHub pricing announcements"] |
| [E.g., "AI agents support structured file workflows"] | High | [E.g., "Test with 2+ agents before launch"] |
| [E.g., "Target users are GitHub-literate"] | Medium | [E.g., "Validate in Phase 1 usability tests"] |
| [E.g., "Demand for templates continues growing"] | Medium | [E.g., "Track Notion/Gumroad marketplace trends"] |

---

## Non-Goals *(mandatory)*

<!--
  Explicitly state what you are NOT building to prevent scope creep.
  Review at phase transitions and update as scope evolves.
-->

**Not building in this phase**:
- [E.g., "Automated quality checks - manual curation for MVP"]
- [E.g., "Advanced search/filters - basic browse only"]
- [E.g., "User accounts/profiles - GitHub OAuth only"]

**Not targeting**:
- [E.g., "Enterprise IT procurement teams - PLG focus only"]
- [E.g., "Individual hobbyists without professional workflow pain"]

**Deferred to post-PMF**:
- [E.g., "Payment processing and monetization"]
- [E.g., "Private/team workspaces"]
- [E.g., "API access for integrations"]

---

## Distribution & Adoption Hypotheses *(mandatory)*

### Primary Channel Hypothesis

- **Channel**: [E.g., "Product Hunt launch for early adopter visibility"]
- **Rationale**: [Why this channel reaches our persona most efficiently]
- **Success criterion**: [E.g., "100+ high-quality signups in first week"]

### Secondary Channels (Ordered by Priority)

1. [E.g., "Twitter/X: Problem-solution storytelling to micro-community"]
2. [E.g., "Communities (Reddit, Discord): Direct engagement with target segment"]
3. [E.g., "Content: Long-form examples showing hero workflow in action"]

### Viral/Network Hypothesis

- **Does collaboration/sharing drive value?** [Yes/No - explain briefly]
- **If yes**: [E.g., "Users share workflows with teammates → encourages team sign-up"]
- **If no**: [E.g., "Individual-use only; focus on word-of-mouth from power users"]

### Early Adopter Profile

- **Who jumps at this first?** [E.g., "Frustrated power users in niche communities"]
- **Where to find them?** [E.g., "r/[subreddit], Twitter threads about [problem], Discord communities"]
- **How to activate them?** [E.g., "Direct outreach + early access + high-touch onboarding"]

---

## Success Criteria for Discovery Phase *(mandatory)*

Before proceeding to research planning, we consider discovery successful when:

- [ ] **Persona Validation**: Conducted 10-20 interviews; personas feel distinct and real
- [ ] **JTBD Clarity**: Top 3 JTBD consistently mentioned; evidence of willingness to pay evident
- [ ] **Hero Workflow Buy-In**: 5+ users manually validated workflow end-to-end; "wow moment" observed
- [ ] **Metrics Feasibility**: Can instrument all success metrics within our tech constraints
- [ ] **Risk Acknowledgment**: Top 3 risks explicitly stated and mitigation plans drafted
- [ ] **Go-to-Market Confidence**: Primary channel identified and testable in < 2 weeks

---

## Open Questions *(prioritized)*

<!--
  Questions to resolve before committing to a full research plan.
  These will be prioritized in /pmfkit.clarify
  Each question should have priority, decision owner, and timeline.
-->

| Priority | Question | Decision Owner | Resolve By |
|----------|----------|----------------|------------|
| P1 | [E.g., "Is hero workflow achievable in <5 min or closer to 15 min?"] | [Product Lead] | [Phase 1 Week 2] |
| P1 | [E.g., "Which persona segment has highest willingness-to-pay?"] | [Research Lead] | [Phase 1 Week 4] |
| P2 | [E.g., "Do power users prefer collaboration or individual use?"] | [Product Lead] | [Phase 2] |
| P3 | [E.g., "Should we support private kits in MVP?"] | [Eng Lead] | [Post-Phase 2] |

---

## AI Product References

<!--
  Reference successful AI products to anchor expectations and patterns.
  Show that our hero workflow and success metrics are grounded in proven PMF.
-->

**Products with similar hero workflows** (for pattern reference):
- [E.g., "Cursor: IDE autocomplete → time saving in coding → adoption through dev community"]
- [E.g., "Runway: Text-to-video in creative tool → render time reduction → viral creator adoption"]
- [E.g., "Harvey: Legal document analysis → time saving for lawyers → enterprise sales + PLG"]

**Key PMF patterns we're following**:
- [E.g., "Product-led growth: free tier with workflow limits drives self-serve discovery"]
- [E.g., "Community validation: early adopter community energizes brand + provides feedback loop"]

---

## Constitution Alignment *(mandatory)*

Verify alignment with PMF-Kit constitution principles (`.pmf/memory/constitution.md`):

- [ ] **Principle I (Specification-First)**: Hypotheses defined before experiments
- [ ] **Principle II (Customer-Evidence-Driven)**: Success criteria include measurable customer behavior
- [ ] **Principle III (Iterative Validation)**: Stories independently testable with clear success/failure criteria
- [ ] **Principle IV (Minimal Viable Process)**: Simplest process justified; qualitative before quantitative
- [ ] **Principle V (Cross-Functional)**: Technical feasibility and GTM implications addressed
- [ ] **Principle VI (Namespace Isolation)**: Correct command prefixes used
- [ ] **Principle VII (Template Extensibility)**: Adaptable patterns documented
- [ ] **Principle VIII (Continuous Optimization)**: Optimization checkpoints planned

---

## Next Steps

**Immediate**: Run `/pmfkit.clarify` to resolve P1 open questions

**If clarification passes**: Run `/pmfkit.plan` to design research methodology and validation experiments

**If risks are high**: Run targeted hero workflow validation interviews (5-10 users) before full research planning

**At phase transitions**: Run `/pmfkit.optimize` to refine hypotheses based on learnings
