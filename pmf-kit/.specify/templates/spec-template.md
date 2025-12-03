# PMF Specification: [PRODUCT NAME]

**Feature Branch**: `[###-pmf-discovery]`
**Created**: [DATE]
**Status**: Draft
**Discovery Focus**: [AI Product Category]

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

### Primary Persona: [Persona 1 - Role/Title]

**Context**:
- **Role**: [Specific title/function]
- **Company**: [Size, industry, stage] - e.g., "Mid-market B2B SaaS, Series A"
- **Team**: [Who they collaborate with]
- **Tools they use**: [Current toolchain]
- **Success metric**: [What success looks like in their role]

**Pain Profile**:
- **Top pain**: [Most acute problem frequency & impact]
- **Current workaround**: [How they solve it today]
- **Willingness to try**: [Signal of openness - why they're looking]

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

**Evidence of willingness-to-pay**: [Signal - complaint in community, switching cost, etc.]

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

- [E.g., "% of signups completing hero workflow in first session"]
- [E.g., "% creating first artifact within 24 hours"]

### Engagement Metrics

- [E.g., "Frequency: workflows per active user per week"]
- [E.g., "Depth: % of users trying advanced features"]

### Retention Metrics

- [E.g., "Day-7 / Day-30 retention of activated users"]
- [E.g., "Monthly active user churn rate"]

### AI-Specific Metrics

- [E.g., "Quality of AI output as rated by users (1-5 scale)"]
- [E.g., "% of outputs used without modification"]
- [E.g., "User confidence in AI results (survey signal)"]

### Business Metrics

- [E.g., "Willingness to pay (free vs paid signup ratio)"]
- [E.g., "LTV / CAC ratio target"]
- [E.g., "Viral coefficient (new users per user)"]

### PMF Validation Threshold

- [E.g., "Sean Ellis test: 40%+ of users would be disappointed without product"]
- [E.g., "Retention: 30%+ D30 for core segment"]
- [E.g., "NPS: > 50 from activated users"]

---

## Constraints & Risks *(mandatory)*

### Technical Feasibility

- [E.g., "AI accuracy must be >= 85% for use case to be viable"]
- [E.g., "Latency requirement: < 3 seconds for workflows to feel instant"]
- [E.g., "Data privacy: GDPR-compliant, no training on user data without consent"]

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

## Open Questions

<!--
  Questions to resolve before committing to a full research plan.
  These will be prioritized in /pmfkit.clarify
-->

- [E.g., "Is the hero workflow achievable in < 5 minutes, or closer to 15 minutes?"]
- [E.g., "Do power users prefer collaboration features, or is this individual-use only?"]
- [E.g., "Which persona segment has highest willingness-to-pay?"]

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

## Next Steps

**Immediate**: Run `/pmfkit.clarify` to resolve top 3 open questions

**If clarification passes**: Run `/pmfkit.plan` to design research methodology and validation experiments

**If risks are high**: Run targeted hero workflow validation interviews (5-10 users) before full research planning
