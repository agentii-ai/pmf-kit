# PMF Research Plan: [PRODUCT NAME]

**Feature Branch**: `[###-pmf-discovery]`  
**Created**: [DATE]  
**Status**: Draft  
**Discovery Phase**: [Phase 0: Foundations / Phase 1: Persona-Problem / Phase 2: Workflow Validation / Phase 3: Go-to-Market]  
**Plan Owner**: [Name/Role]

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
- Success threshold: [E.g., "≥75% of test users complete workflow in ≤5 min with satisfaction ≥4/5"]
- Evidence source: [E.g., "Moderated hero workflow testing sessions (N=10)"]

**Question 3**: [E.g., "Is there genuine willingness-to-pay for our solution vs. free alternatives?"]
- Hypothesis: [E.g., "Users value our solution enough to pay $5-20/mo"]
- Success threshold: [E.g., "≥40% indicate WTP in interviews; ≥50% mention specific incumbent pain points"]
- Evidence source: [E.g., "WTP probes in interviews + landing page conversion"]

**Question 4**: [E.g., "Can creators complete the submission workflow with acceptable satisfaction?"]
- Hypothesis: [E.g., "Creators can submit in <5 min with ≥4/5 satisfaction"]
- Success threshold: [E.g., "≥80% complete submission; ≥70% rate curation feedback 4+ stars"]
- Evidence source: [E.g., "Creator workflow usability tests (N=8)"]

**Question 5**: [E.g., "Do network effects exist? Does more supply drive more demand?"]
- Hypothesis: [E.g., "Each new kit submission drives 5+ new users"]
- Success threshold: [E.g., "R² > 0.4 correlation between kit count and user signups; ≥10% cross-side conversion"]
- Evidence source: [E.g., "Behavioral analytics during Phase 3 beta"]

**Question 6**: [E.g., "Which distribution channel delivers highest-quality users?"]
- Hypothesis: [E.g., "Product Hunt drives volume; communities drive quality (D7 retention)"]
- Success threshold: [E.g., "Identify 1-2 channels with activation ≥15% AND D7 retention ≥30%"]
- Evidence source: [E.g., "Multi-channel launch with UTM tracking + cohort analysis"]

### Research Phases & Exit Criteria

Research progresses through PDCA cycles (Plan → Do → Check → Act) at 2-4 week intervals.

**Phase 0 – Foundations**: Align team, instrument metrics, recruit participant pipeline
**Phase 1 – Problem Validation**: 15-20 interviews; persona + JTBD confirmed
**Phase 2 – Workflow Validation**: 8-10 usability tests; hero workflow meets TTFW target
**Phase 3 – Channel Validation**: Test 2-3 channels; identify highest-PMF acquisition path

---

## Constitution Check *(mandatory)*

Verify alignment with PMF-Kit principles (`.pmf/memory/constitution.md`):

- [ ] **Principle I (Specification-First)**: Research questions tied to PMF spec hypotheses
- [ ] **Principle II (Customer-Evidence-Driven)**: Direct evidence (interviews, behavior, not assumptions)
- [ ] **Principle III (Iterative Validation)**: Independent checkpoints; go/kill/pivot gates
- [ ] **Principle IV (Minimal Viable Process)**: Qualitative → quantitative; manual before automated
- [ ] **Principle V (Cross-Functional)**: Incorporates product, growth, design, community perspectives
- [ ] **Principle VI (Namespace Isolation)**: Correct command prefixes; no conflicts
- [ ] **Principle VII (Template Extensibility)**: Patterns adaptable to other domains
- [ ] **Principle VIII (Continuous Optimization)**: `/pmfkit.optimize` checkpoints planned

---

## Budget & Resources *(mandatory)*

### Participant Incentives

| Activity | Participants | Incentive | Total |
|----------|--------------|-----------|-------|
| Phase 1 Interviews | N=20 | $50/person | $1,000 |
| Phase 2 Usability Tests | N=10 | $50/person | $500 |
| Phase 3 Beta Testers | N=50+ | Early access | $0 |
| **Total Budget** | | | **$1,500+** |

### Tools & Platforms

- **Interviews**: [Zoom, Calendly]
- **Synthesis**: [Notion, Typeform]
- **Analytics**: [Vercel Analytics, GitHub API]
- **Landing Page**: [Vercel deployment]

---

## Risk Mitigation *(mandatory)*

| Risk | Impact | Mitigation | Fallback |
|------|--------|------------|----------|
| Participant recruitment fails (<15 interviews) | High | Increase incentive $50→$75; expand sourcing channels; snowball sampling | Extend Phase 1 by 2 weeks; accept N=15 if patterns saturate |
| GitHub barrier insurmountable (<50% completion) | High | Test web UI alternative; create video walkthroughs | Target technical users first; expand to non-technical later |
| No clear winner channel (all <15% activation) | Medium | Test 2 additional channels; revisit value prop | Try direct sales if PLG fails |
| Network effects don't materialize (R² <0.4) | Medium | Add explicit sharing CTAs; investigate if kits are being shared | Pivot to single-side model (B2C SaaS) |

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

**Multi-Agent Compatibility Testing**:
- Test hero workflow on 2+ AI agents (Claude Code, Cursor minimum)
- N=5 test runs per agent per workflow
- Measure: First-run success rate, errors encountered, agent-specific workarounds
- Success threshold: ≥80% cross-agent compatibility without modification

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

**Network Effects Measurement** (if marketplace):
- Track: Kit submission events → spike in user signups (7-day window)
- Track: User cohort → % who submit a kit within 30 days (cross-side conversion)
- Calculate: R² correlation between kit count and user signups
- Target: R² > 0.4 for Phase 3; R² > 0.6 at scale

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
**Duration**: 45 min

**Agenda**:
1. **Metrics Review** (10 min): Phase-specific numbers (interviews completed, TTFW data, channel performance)
2. **Learnings** (15 min): Quotes, patterns, surprises, contradictory evidence
3. **Blockers** (10 min): Participant no-shows, tool issues, unclear findings
4. **Decisions** (5 min): Pivot signals? Adjust questions? Extend phase?
5. **Next Week Focus** (5 min): Task assignments, PDCA "Do" priorities

**Output**: Updated Notion dashboard + task priorities + documented decisions

### Phase-End Review (Every 4 Weeks)

**Decision**: Does this phase exit criteria pass?
- If YES → Advance to next phase
- If PIVOT → Adjust focus and re-run phase
- If NO-GO → Kill hypothesis; explore alternative

---

## Phase 4: Research Archive (Required)

**Goal**: Preserve research artifacts for future reference and stakeholder communication

**Duration**: 1 week post-Phase 3 | **Owner**: [Research Lead]

**Activities**:
- De-identify interview transcripts (remove names, company info)
- Compile quote library organized by hypothesis/persona
- Create internal briefing document (1-page executive summary + 5-10 page detailed findings)
- Archive raw data with 12-month retention policy
- Document lessons learned for methodology improvement

**Deliverables**:
- `research-artifacts/transcripts-de-identified/`
- `research-artifacts/quote-library.md`
- `research-artifacts/phase-summary.md` (per phase)
- `research-artifacts/lessons-learned.md`

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
| 3: Network | Kit → user correlation (if marketplace) | R² > 0.4 |
| 3: Network | Cross-side conversion (if marketplace) | ≥10% |

---

## Critical Path

**Phase Dependencies**:
- Phase 0 MUST complete before Phase 1 (need participants recruited + instruments ready)
- Phase 1 MUST complete before Phase 2 (need validated personas + JTBD before testing workflows)
- Phase 2 MUST complete before Phase 3 (need successful hero workflow before channel testing)

**Timeline**:
- Phase 0: 2 weeks
- Phase 1: 4 weeks
- Phase 2: 3 weeks
- Phase 3: 4-6 weeks
- Phase 4: 1 week
- **Total**: 14-16 weeks for full PMF discovery cycle

---

## Next Steps

1. **Confirm Phase 0 tasks** (align team, recruit, instrument metrics)
2. **Run `/pmfkit.tasks`** to generate detailed task breakdown for Phase 1 interviews
3. **Execute Phase 1** (4-week sprint)
4. **Review Phase 1 exit criteria** → decide Phase 2 advancement
5. **At phase transitions**: Run `/pmfkit.optimize` to refine hypotheses based on learnings
