# PMF Research Plan: [PRODUCT NAME]

**Feature Branch**: `[###-pmf-discovery]`
**Created**: [DATE]
**Status**: Draft
**Discovery Phase**: [Phase 0: Foundations / Phase 1: Persona-Problem / Phase 2: Workflow Validation / Phase 3: Go-to-Market]

---

## Research Context *(mandatory)*

<!--
  Define the research strategy: what questions we're answering, who we're learning from,
  and how we'll collect evidence. This is NOT technical architecture - it's learning strategy.
-->

### Primary Research Questions

**Question 1**: [E.g., "Do our target personas actually have the JTBD we think they do?"]
- Hypothesis: [E.g., "Personas spend 2+ hours per week on workaround"]
- Success threshold: [E.g., "80% of interviewed personas report this frequency"]
- Evidence source: [E.g., "In-depth interviews (30-60 min, N=15)"]

**Question 2**: [E.g., "Can our hero workflow be executed in < 5 minutes with acceptable quality?"]
- Hypothesis: [E.g., "User can complete workflow end-to-end in 5 min or less"]
- Success threshold: [E.g., "10/10 test users complete workflow in <= 5 min with satisfaction >= 4/5"]
- Evidence source: [E.g., "Moderated hero workflow testing sessions"]

### Research Phases & Exit Criteria

Research progresses through PDCA cycles (Plan → Do → Check → Act) at 2-4 week intervals.

**Phase 0 – Foundations**: Align team, instrument metrics, recruit participant pipeline
**Phase 1 – Problem Validation**: 15-20 interviews; persona + JTBD confirmed
**Phase 2 – Workflow Validation**: 8-10 usability tests; hero workflow meets TTFW target
**Phase 3 – Channel Validation**: Test 2-3 channels; identify highest-PMF acquisition path

---

## Constitution Check *(mandatory)*

Verify alignment with PMF-Kit principles (/memory/constitution.md):

- [ ] **Specification-First**: Research questions tied to PMF spec hypotheses
- [ ] **Customer-Evidence-Driven**: Direct evidence (interviews, behavior, not assumptions)
- [ ] **Iterative Validation**: Independent checkpoints; go/kill/pivot gates
- [ ] **Minimal Viable Process**: Qualitative → quantitative; manual before automated
- [ ] **Cross-Functional**: Incorporates product, growth, design, community perspectives

---

## Phase 1: Problem & Persona Validation

**Goal**: Confirm personas and JTBD are real, urgent, and worth solving

**Duration**: 4 weeks | **Owner**: [Name]

**Research Activities**:
- In-depth interviews: N=15-20 with target persona
- Duration: 45-60 min per interview
- Topics: Role/context → current workflow → pain frequency/intensity → workaround satisfaction
- Deliverable: Interview synthesis document with persona validation and JTBD evidence

**Evidence Collection Instrument**:
```
Interview Guide:
1. [Opening] Establish rapport, confirm they work in [domain]
2. [Current workflow] "Walk me through how you currently solve [JTBD]"
3. [Pain signals] "How often do you do this? How long does it take? What frustrates you?"
4. [Willingness to try] "If there were a better way, what would make it worth your time?"
5. [Closing] Capture quote + contact for potential phase 2 testing
```

**Weekly PDCA**:
- **Do**: Conduct 3-4 interviews
- **Check**: After 5 interviews, are patterns emerging? Revise questions if needed.
- **Act**: Adjust persona definition or JTBD priority

**Phase 1 Exit Criteria** (Go/No-Go):
- [ ] **GO**: 70%+ personas report pain frequency 2+x/week; willingness to try evident
- [ ] **NO-GO**: Pain signals weak; explore adjacent personas
- [ ] **PIVOT**: Different JTBD emerges as higher priority; refocus

**Successful Phase 1 Output**:
- Validated personas with quotes
- Top 3 JTBD with evidence
- Willingness-to-pay signals documented
- Participant pool for Phase 2

---

## Phase 2: Hero Workflow Validation

**Goal**: Ensure hero workflow delivers value; user can execute end-to-end

**Duration**: 3 weeks | **Owner**: [Name]

**Research Activities**:
- Moderated usability tests: N=8-10 target users
- Duration: 45 min per session
- Setup: User performs hero workflow with real/representative data
- Measures: TTFW, task completion, satisfaction (1-5 scale), quote capture

**Evidence Collection Instrument**:
```
Usability Testing Script:
1. [Intro] "We're testing a new workflow to [goal]. Think aloud as you work."
2. [Setup] "Here's the scenario: [describe context, give them artifact/data]"
3. [Tasks] "Try completing [hero workflow steps]"
4. [Probes] "What confused you? What went well?"
5. [Satisfaction] "Would you use this if it existed? Why/why not?"
6. [Quote] Capture 1-2 verbatim reactions
```

**Weekly PDCA**:
- **Do**: Run 2-3 tests
- **Check**: After 3-4 tests, are friction points clear? Top feedback themes?
- **Act**: Quick non-technical fixes (copy, order, defaults); re-test

**Phase 2 Exit Criteria** (Go/Kill/Pivot):
- [ ] **GO**: 75%+ users complete workflow; TTFW < [target]; satisfaction >= 4/5
- [ ] **NO-GO**: Workflow too complex; core value unclear; redesign needed
- [ ] **PIVOT**: Workflow works for segment 2 but not 1; shift focus

**Successful Phase 2 Output**:
- Usability test summary with quotes
- Friction points identified + prioritized
- TTFW measurement vs target
- Participant pool for Phase 3 (channel testing)

---

## Phase 3: Channel & Acquisition Testing

**Goal**: Validate repeatable, scalable acquisition path

**Duration**: 4 weeks | **Owner**: [Growth]

**Research Activities**:
- Launch on 2-3 channels (e.g., Product Hunt + Twitter + Communities)
- Measure: Channel CAC, activation rate, Day-7 retention by segment
- Track: Signup → hero workflow start → completion → satisfaction

**Weekly PDCA**:
- **Do**: Campaign executes; track daily metrics
- **Check**: Which channel + segment combo has best activation?
- **Act**: Double down on best, kill low performers

**Phase 3 Exit Criteria** (Go/Scale/Pivot):
- [ ] **GO**: Activation 15%+, D7 retention 25%+; clear winner channel + segment
- [ ] **SCALE**: Metrics show repeatable path; ready for broader launch
- [ ] **PIVOT**: Activation < 10%; need to revisit value prop or hero workflow

**Successful Phase 3 Output**:
- Channel performance summary
- Cohort analysis by segment
- Validated acquisition playbook for strongest channel
- Go/no-go decision on scaling

---

## Validation Checkpoints & Rituals

### Weekly PMF Review (Every Monday)

**Attendees**: Product, Growth, Design, Community  
**Duration**: 30-60 min

**Agenda**:
1. **Metrics**: Which signals moved this week?
2. **Learnings**: What did we discover about personas, workflow, or channels?
3. **Blockers**: What's slowing research?
4. **Next week**: What's the focus for PDCA Do?

**Output**: Updated task priorities + any pivot decisions

### Phase-End Review (Every 4 Weeks)

**Decision**: Does this phase exit criteria pass?
- If YES → Advance to next phase
- If PIVOT → Adjust focus and re-run phase
- If NO-GO → Kill hypothesis; explore alternative

---

## Success Criteria Summary

| Phase | Success Metric | Go Threshold |
|-------|----------------|--------------|
| 1: Problem | % personas with 2+x/week pain | 70%+ |
| 1: Problem | Willingness-to-try signal | Mentioned by 60%+ |
| 2: Workflow | % completing hero workflow end-to-end | 75%+ |
| 2: Workflow | TTFW vs target | Meet < [target] time |
| 2: Workflow | User satisfaction (1-5 scale) | >= 4.0 avg |
| 3: Channel | Activation rate | 15%+ |
| 3: Channel | Day-7 retention | 25%+ |
| 3: Channel | Clear winner channel | 2x+ better than 2nd |

---

## Next Steps

1. **Confirm Phase 0 tasks** (align team, recruit, instrument metrics)
2. **Run `/pmfkit.tasks`** to generate detailed task breakdown for Phase 1 interviews
3. **Execute Phase 1** (4-week sprint)
4. **Review Phase 1 exit criteria** → decide Phase 2 advancement
