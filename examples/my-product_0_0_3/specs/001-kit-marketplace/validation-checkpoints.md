# Phase 1: Validation Checkpoints & Go/No-Go Thresholds

**Feature**: agentii-kit marketplace platform
**Branch**: `001-kit-marketplace`
**Created**: 2025-12-04
**Purpose**: Define PDCA cycle gates, decision criteria, and pivot triggers for Phase 1 research (Problem & Persona Validation)

---

## Overview: PDCA Decision Framework

Phase 1 research runs over **4 weeks** with **weekly checkpoints** following Plan-Do-Check-Act cycles:

| Week | Cycle | Activity | Checkpoint |
|------|-------|----------|-----------|
| Week 1 | Plan | Recruit participants; refine instruments | Recruitment on track? |
| Week 2 | Do | Conduct creator interviews; practitioner interviews | 50% interviews complete? |
| Week 3 | Check | Conduct usability tests; analyze feedback | Patterns emerging? |
| Week 4 | Act | Compile findings; recommend go/no-go/pivot | Meet success thresholds? |

---

## Hypothesis-Level Validation Checkpoints

Each hypothesis has explicit Go/No-Go/Pivot criteria. Decisions are made by: [Product Lead] + [Research Lead] + [Stakeholder]

---

### Checkpoint 1: Creator JTBD Hypothesis Block (Week 2, end of interviews)

**Hypotheses being validated**:
- H1.1: Domain experts feel acute pain sharing knowledge
- H1.2: Creators are motivated by recognition, not revenue

**Data Collection**:
- 12-15 creator interviews (60 min each)
- Feedback synthesis: pain points, motivation signals, willingness to publish

**GO Criteria** (All must pass):

| Metric | Threshold | Evidence |
|--------|-----------|----------|
| Pain frequency | ≥70% report monthly+ pain with current workflows | Interview transcript: "How often do you share?" → 70%+ say weekly/monthly/quarterly |
| Pain severity | ≥70% rate pain ≥4/5 on pain scale | Interview: pain scale question → average ≥4/5 |
| Recognition motivation | ≥80% prioritize recognition over revenue | Interview: motivation question → 80%+ choose "recognition scenario" |
| Willingness to publish free | ≥70% would publish on free platform if visibility high | Interview: "Would you publish on agentii-kit free if visibility high?" → 70%+ yes |
| Current workaround ineffectiveness | ≥75% dissatisfied with current tools | Interview: "Rate satisfaction with current tools 1-5" → avg ≤3/5 |

**Sample Decision Matrix**:

| Outcome | Action |
|---------|--------|
| **GO**: 4-5 metrics pass | Proceed to usability test (H1.3). Assume creator JTBD is real. |
| **PIVOT**: 2-3 metrics pass | Deep-dive interviews with non-adopters. Hypothesis may be asymmetric (e.g., only legal experts, not others). Adjust persona segmentation. |
| **NO-GO**: ≤1 metric passes | Creator JTBD is not urgent enough. Consider pausing kit marketplace; explore other hypotheses. |

**Decision Authority**: [Product Lead] + [Stakeholders]

**Timeline**: Week 2, end of day Wednesday

---

### Checkpoint 2: User JTBD Hypothesis Block (Week 2, end of interviews)

**Hypotheses being validated**:
- H2.1: Practitioners feel pain finding & adopting expert workflows
- H2.2: Practitioners value time savings & quality improvement

**Data Collection**:
- 12-15 practitioner interviews (45 min each)
- Feedback synthesis: workflow pain, time waste, willingness to adopt

**GO Criteria**:

| Metric | Threshold | Evidence |
|--------|-----------|----------|
| Workflow pain frequency | ≥75% report monthly+ pain with current processes | Interview: "How often do you repeat similar workflows?" → 75%+ say monthly+ |
| Time waste per project | ≥70% report 5+ hours lost per project | Interview: "Hours wasted on repetition?" → avg ≥5 hours |
| Willingness to use kit | ≥80% would "definitely" or "very likely" use a kit | Interview: "Would you use a kit like this?" → 80%+ say yes/definitely |
| Adoption motivation | ≥75% prioritize time savings or quality | Interview: "What would motivate you?" → 75%+ say time/quality (not price) |
| Current workaround frustration | ≥70% dissatisfied with cobbling together templates | Interview: workaround satisfaction ≤3/5 |

**Decision Matrix**:

| Outcome | Action |
|---------|--------|
| **GO**: 4-5 metrics pass | Proceed to usability test (H2.3). Assume user JTBD is real. |
| **PIVOT**: 2-3 metrics pass | User pain exists but may be role-specific. Adjust segmentation. Consider focusing on 1-2 high-pain roles first (e.g., legal, PM). |
| **NO-GO**: ≤1 metric passes | User JTBD insufficient. Platform may not address real pain. Reconsider market opportunity. |

**Decision Authority**: [Product Lead] + [Stakeholders]

**Timeline**: Week 2, end of day Wednesday

---

### Checkpoint 3: Hero Workflow Feasibility (Week 3, usability tests)

**Hypotheses being validated**:
- H1.3: Kit creator can publish in <30 min
- H2.3: Kit user can go discovery→fork→customize→execute in <15 min

**Data Collection**:
- Usability test 1: 5-8 creators attempting to publish (moderated)
- Usability test 2: 8-10 users attempting full workflow (moderated)
- Measurement: time to completion, errors, satisfaction, output quality

**GO Criteria for Creator Workflow**:

| Metric | Threshold | Evidence |
|--------|-----------|----------|
| Time to completion | ≥70% complete in <30 min | Test observation: timer measurement |
| Output quality | ≥70% output is "publishable" (constitution + templates + example + README) | Facilitator assessment: all sections filled in? |
| Satisfaction | Average satisfaction ≥4/5 | Post-test question: "Rate your satisfaction 1-5" |
| Clarity of instructions | Average instruction clarity ≥4/5 | Post-test: "Clarity of instructions 1-5" |
| Recommend iterations | ≥70% say "I would publish this as-is" | Post-test: "Would you publish this?" |

**Decision Matrix**:

| Outcome | Action |
|---------|--------|
| **GO**: 4-5 metrics pass | Creator workflow is feasible. Proceed to Phase 2. |
| **PIVOT**: 2-3 metrics pass | Workflow is close but needs refinement. Consider: (1) Providing better templates/examples, (2) Adding UI scaffolding, (3) Extending TTFW to 45 min. Run 2 more iterations. |
| **NO-GO**: ≤1 metric passes | <30 min is not achievable. Re-evaluate TTFW target. Consider 45-60 min as realistic. |

**GO Criteria for User Workflow**:

| Metric | Threshold | Evidence |
|--------|-----------|----------|
| Time to completion | ≥75% complete in <15 min | Test observation: timer measurement |
| Useful output generated | ≥70% generate output they rate ≥3/5 quality | Test observation + post-test assessment |
| Satisfaction | Average satisfaction ≥4/5 | Post-test: "Rate experience 1-5" |
| Repeat usage intent | ≥70% would use kit again | Post-test: "Would you use this kit for future projects?" → yes |
| NPS | Net Promoter Score ≥30 | Post-test: "Recommend to colleague 1-10" → (% 9-10) - (% 0-6) |

**Decision Matrix**:

| Outcome | Action |
|---------|--------|
| **GO**: 4-5 metrics pass | User workflow is feasible. Proceed to Phase 2 (Workflow Validation at scale). |
| **PIVOT**: 2-3 metrics pass | Workflow close but needs iteration. Pinpoint friction (discovery? fork? customize? agent integration?). Fix and retest. |
| **NO-GO**: ≤1 metric passes | <15 min is not achievable. Consider longer TTFW or workflow redesign. May indicate fundamental friction (e.g., agent compatibility issues). |

**Decision Authority**: [Product Lead] + [Design Lead]

**Timeline**: Week 3, end of day Friday

---

### Checkpoint 4: Market & Distribution Hypothesis Block (Weeks 2-3, exploratory)

**Hypotheses being validated**:
- H3.1: Demand for template marketplaces is real
- H3.2: AI agent adoption is at inflection point
- H5.1: Product Hunt + GitHub launch can drive adoption
- H5.2: Early adopters match personas

**Data Collection**:
- Community outreach interviews (10-15 influencers/community leaders)
- Survey of existing template users (N=100-200)
- GitHub/Reddit trends analysis
- Beta tester feedback pre-launch (N=50-100)

**GO Criteria**:

| Metric | Threshold | Evidence |
|--------|-----------|----------|
| Template marketplace demand | ≥60% of existing template users want better discoverability/collaboration | Survey: "What's missing in current marketplaces?" |
| Influencer willingness to share | ≥70% of community leaders willing to share on launch day | Outreach interview: "Would you share this with your community?" |
| AI agent comfort | ≥60% of practitioners comfortable with agent-based workflows | Survey + interview: "Would you use AI agent workflows?" |
| Beta tester enthusiasm | ≥80% of beta testers rate platform ≥4/5 | Beta feedback: satisfaction |
| Community fit | ≥70% of early adopters expected from target communities (spec-kit, agents, productivity) | Referral source analysis |

**Decision Matrix**:

| Outcome | Action |
|---------|--------|
| **GO**: 4-5 metrics pass | Market signals are strong. Proceed with Product Hunt + GitHub launch strategy. |
| **PIVOT**: 2-3 metrics pass | Market interest exists but may be concentrated (e.g., strong in spec-kit/agent communities, weak in others). Adjust launch channels. Consider soft-launch to high-interest communities first. |
| **NO-GO**: ≤1 metric passes | Market signals weak. Consider: (1) Delayed public launch, (2) Longer beta period, (3) Different GTM strategy (e.g., B2B partnerships instead of viral launch). |

**Decision Authority**: [Product Lead] + [Marketing Lead]

**Timeline**: Week 3, end of day Friday

---

### Checkpoint 5: Multi-Agent Compatibility (Week 3, technical validation)

**Hypothesis being validated**:
- H4.1: Multi-agent compatibility is technically feasible

**Data Collection**:
- Functional testing: 2 reference kits (PM-Kit, Marketing-Kit) executed on 2+ agents
- User testing: 5-10 real users per agent (Claude Code, Cursor)
- Error logging and issue tracking

**GO Criteria**:

| Metric | Threshold | Evidence |
|--------|-----------|----------|
| Cross-agent compatibility | ≥80% of kits work first-try on 2+ agents | Test execution: success rate |
| Agent-specific fixes needed | <5% of issues require kit modification | Issue tracking: agent-specific problems |
| User success rate | ≥80% of users successfully execute workflow on their agent | User test observation |
| Documentation clarity | ≥70% of users don't need help with agent setup | User test: facilitator assistance needed? |

**Decision Matrix**:

| Outcome | Action |
|---------|--------|
| **GO**: 4 metrics pass | Multi-agent support is achievable. Target all major agents in MVP. |
| **PIVOT**: 2-3 metrics pass | Focus on 1-2 best-performing agents in MVP (e.g., Claude Code + Cursor). Add others in Phase 2. |
| **NO-GO**: ≤1 metric passes | Multi-agent complexity is higher than expected. Recommend single-agent MVP (e.g., Claude Code only) to launch faster; add agents post-launch. |

**Decision Authority**: [Engineering Lead] + [Product Lead]

**Timeline**: Week 3, end of day Friday

---

## Phase 1 Exit Criteria (Week 4 Synthesis)

### All Hypotheses Block Decision

After all checkpoints are evaluated, make a **Go/No-Go/Pivot decision for Phase 1 overall**:

**GO to Phase 2** (Workflow Validation):
- Creator JTBD checkpoint: GO
- User JTBD checkpoint: GO
- Hero Workflow Feasibility checkpoint: GO (both creator + user)
- Market signals checkpoint: GO or PIVOT (acceptable)

**PIVOT to Phase 1.5** (Refinement + Re-test):
- 1-2 checkpoints in PIVOT territory
- Others are GO
- Action: Implement refinements, re-test 1-2 hypotheses, then proceed to Phase 2

**NO-GO / Pause**:
- ≥2 checkpoints in NO-GO territory
- Action: Deep-dive into failure signals. Consider product redesign, target segment shift, or strategic pivot.

### Phase 1 Success Checklist

- [x] All interviews conducted and synthesized (Creator + User + Influencer)
- [x] Usability tests completed (Creator workflow + User workflow)
- [x] Multi-agent technical validation done
- [x] Market signal survey completed
- [x] All checkpoints evaluated against criteria
- [x] Go/No-Go/Pivot decision documented
- [x] Findings compiled into executive summary
- [x] Next phase (Phase 2) planning initiated if GO

### Findings Synthesis Document

By end of Week 4, produce:

1. **Executive Summary** (1 page):
   - Key findings: Do personas exist? Is pain real? Are workflows feasible?
   - Go/No-Go/Pivot decision
   - Recommended next phase

2. **Detailed Findings Report** (5-10 pages):
   - Creator JTBD findings
   - User JTBD findings
   - Hero workflow insights (friction points, opportunities)
   - Market readiness assessment
   - Agent compatibility results
   - Persona segmentation (any adjustments?)

3. **Pivot Signals** (if applicable):
   - What surprised us?
   - Which hypotheses didn't validate?
   - Recommended adjustments

4. **Phase 2 Research Plan** (if GO):
   - Workflow validation approach
   - Channel validation plan
   - Launch readiness timeline

---

## Decision Authority & Escalation

### Level 1: Checkpoint Decision (Weekly)
- **Owner**: [Research Lead]
- **Review**: [Product Lead]
- **Authority**: Decide go/pivot for that specific checkpoint

### Level 2: Phase 1 Exit Decision (Week 4)
- **Owner**: [Product Lead]
- **Review**: [Stakeholders], [Engineering], [Marketing]
- **Authority**: Decide Go/No-Go/Pivot for Phase 1 overall; green-light Phase 2 or recommend pivot

---

## Contingency Triggers

### If Recruitment Lags

- **Trigger**: By end of Week 1, <30% of target participants recruited
- **Action**: Activate secondary recruitment channels (Upwork, Respondent.io, paid surveys)
- **Escalation**: Notify [Product Lead] if <50% recruited by Day 5

### If Saturation Not Reached

- **Trigger**: By end of Week 2, interviews are still generating new insights (not repeating)
- **Action**: Extend interview count to 20+ per persona (vs. 12-15)
- **Escalation**: Prioritize quick completion to meet Week 3 usability test timeline

### If Usability Test Reveals Major Friction

- **Trigger**: Usability test shows <30% completion rate or average satisfaction <3/5
- **Action**: Conduct rapid iteration (24-48 hr) and retest with 2-3 new participants
- **Escalation**: May indicate need for design overhaul before launch

---

## Next Steps

→ After Week 4 Phase 1 exit decision:

**If GO**: Proceed to Phase 2 (Workflow Validation) to conduct:
- Hero workflow testing at scale (50-100 users)
- Channel validation (soft launches to different communities)
- Retention tracking (first 7-30 days post-launch)

**If PIVOT**: Implement refinements and plan Phase 1.5 re-test cycle

**If NO-GO**: Deep-dive on failure signals; consider strategic pivot or delayed launch
