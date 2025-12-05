# PMF Discovery Task Breakdown: [PRODUCT NAME]

**Branch**: `[###-pmf-discovery]` | **Date**: [DATE] | **Plan**: [link]  
**Tasks Owner**: [Name/Role]

**Overview**: Research and execution tasks organized by learning objective (research questions) and PDCA cycles. Each learning objective has independent validation checkpoints. Tasks marked `[P]` can run in parallel; tasks tagged `[RQ#]` map to specific research questions.

---

## Phase 1: Problem & Persona Validation

**Objective**: Validate personas have real, frequent pain requiring solution

**Duration**: 4 weeks | **Owner**: [Product/Research Lead]

**Exit Criteria**: 15+ interviews conducted; JTBD patterns clear; willingness-to-pay evident

### Task Group 1: Participant Recruitment

- [P] **T1.1** [RQ1] Create screener survey to identify target personas (5-6 questions)
  - Owner: [Research Coordinator]
  - Type: Research prep
  - Deliverable: Screener document at `research-artifacts/screener-survey.md`
  - Due: Day 1

- [P] **T1.2** [RQ1] Build participant recruiting list (30-40 candidates from target channels)
  - Owner: [Research Coordinator]
  - Channels: Twitter #PMLife, Reddit r/ProductManagement, LinkedIn PM groups, Discord communities
  - Deliverable: Outreach list at `research-artifacts/recruitment-list.csv`
  - Due: Day 2

- **T1.3** [RQ1] Recruit and schedule 15-20 interviews (book 3-4 per week)
  - Owner: [Research Coordinator]
  - Incentive: $50/participant (budget: $1,000)
  - Type: Research coordination
  - Deliverable: Interview calendar scheduled + Calendly links
  - Due: End of Week 1

### Task Group 2: Problem-Focused Interviews

- [P] **T1.4** [RQ1] Conduct interviews batch 1 (4-5 interviews, week 1)
  - Owner: [Product Lead]
  - Duration: 45-60 min per interview
  - Deliverable: Interview notes at `research-artifacts/interviews/batch-1/`, recorded (with consent)
  - Due: End of week 1
  - Check: After batch 1, are JTBD patterns emerging? Pain frequency ≥70%?

- [P] **T1.5** [RQ1] Conduct interviews batch 2 (4-5 interviews, week 2)
  - Owner: [Product Lead]
  - Adjust questions based on batch 1 learnings
  - Deliverable: Interview notes at `research-artifacts/interviews/batch-2/`
  - Due: End of week 2
  - Check: Mid-phase decision — continue, pivot persona, or extend?

- **T1.6** [RQ1] Conduct interviews batch 3 (remaining 8-10 interviews, weeks 3-4)
  - Owner: [Product Lead]
  - Deliverable: All interview notes at `research-artifacts/interviews/batch-3/`
  - Due: End of week 4

### Task Group 3: Synthesis & Analysis

- **T1.7** [RQ1] Create JTBD synthesis document
  - Owner: [Product Lead]
  - Content: Top 3 JTBD with supporting verbatim quotes + mention rates + frequency data
  - Deliverable: `research-artifacts/analysis/jtbd-synthesis.md`
  - Due: End of week 3

- **T1.8** [RQ1] Assess persona clarity + refinements
  - Owner: [Product Lead]
  - Validate: Do personas match our assumptions? Calculate % with ≥2 hrs/week pain
  - Deliverable: `research-artifacts/analysis/persona-validation.md`
  - Due: End of week 4

- **T1.9** [RQ3] Document willingness-to-pay signals
  - Owner: [Product Lead]
  - Analyze: What would personas pay? ($X-$Y range); incumbent pain points
  - Deliverable: `research-artifacts/analysis/willingness-to-pay.md`
  - Due: End of week 4

### Phase 1 Checkpoint & Decision Gate

- **T1.10** Phase 1 exit review
  - Decision: Does our persona + JTBD validation meet criteria?
  - Go: 70%+ personas with high-frequency pain → advance to Phase 2
  - Pivot: Different JTBD or persona shows stronger signal → re-target
  - No-Go: Pain signals weak → reconsider positioning
  - Deliverable: Go/pivot/kill decision document
  - Due: End of week 4

---

## Phase 2: Hero Workflow Validation

**Objective**: Validate hero workflow delivers value and meets TTFW target

**Duration**: 3 weeks | **Owner**: [Product/UX Lead]

**Exit Criteria**: 8+ workflow tests; 75%+ completion rate; users see value

### Task Group 1: Usability Test Preparation

- **T2.1** Finalize hero workflow narrative (step-by-step user perspective)
  - Owner: [Product Lead]
  - Content: No technical jargon; clear input → process → output
  - Deliverable: Usability testing script
  - Due: Start of week 1

- **T2.2** Prepare test artifacts and data (realistic sample inputs)
  - Owner: [Product/Design Lead]
  - Content: Representative data for test users
  - Deliverable: Test dataset + example artifacts
  - Due: Start of week 1

- **T2.3** Recruit 10-12 test participants from Phase 1 pool
  - Owner: [Research Coordinator]
  - Compensation: [Coffee gift card / early access / etc.]
  - Deliverable: Test participants scheduled
  - Due: Start of week 1

### Task Group 2: Moderated Usability Testing

- [P] **T2.4** Run usability tests batch 1 (2-3 tests, week 1)
  - Owner: [Facilitator - Product/UX Lead]
  - Measures: TTFW, completion rate, satisfaction, friction points
  - Deliverable: Test video + notes
  - Due: End of week 1
  - Check: After 3 tests, what patterns of friction emerge?

- [P] **T2.5** Run usability tests batch 2 (2-3 tests, week 2)
  - Owner: [Facilitator]
  - Incorporate learnings from batch 1
  - Deliverable: Test video + notes
  - Due: End of week 2

- [P] **T2.6** Run usability tests batch 3 (remaining tests, week 3)
  - Owner: [Facilitator]
  - Deliverable: Test video + notes + completion summary
  - Due: End of week 3

### Task Group 3: Quick Iteration

- **T2.7** Identify top 3 friction points (based on first 3 tests)
  - Owner: [Product Lead]
  - Prioritize: Which friction blocks users most?
  - Deliverable: Friction priority list
  - Due: End of week 1

- **T2.8** Implement non-technical improvements (copy, order, defaults, help text)
  - Owner: [Product/Design Lead]
  - Type: UX refinement (no code implementation)
  - Deliverable: Updated workflow description + new materials
  - Due: End of week 2

### Task Group 4: Multi-Agent Compatibility Testing

- [P] **T2.10** [RQ4] Set up Claude Code test environment
  - Owner: [Engineering Lead]
  - Setup: Install agent, verify commands work, load test kit
  - Deliverable: `research-artifacts/multi-agent/claude-code-setup.md`
  - Due: Week 1

- [P] **T2.11** [RQ4] Set up Cursor test environment
  - Owner: [Engineering Lead]
  - Setup: Install agent, verify commands work, load test kit
  - Deliverable: `research-artifacts/multi-agent/cursor-setup.md`
  - Due: Week 1

- [P] **T2.12** [RQ4] Run hero workflow on Claude Code (N=5 test runs)
  - Owner: [Engineering/QA]
  - Measure: First-run success rate, errors, execution time
  - Deliverable: `research-artifacts/multi-agent/claude-code-results.csv`
  - Due: Week 2

- [P] **T2.13** [RQ4] Run hero workflow on Cursor (N=5 test runs)
  - Owner: [Engineering/QA]
  - Measure: First-run success rate, errors, execution time
  - Deliverable: `research-artifacts/multi-agent/cursor-results.csv`
  - Due: Week 2

- **T2.14** [RQ4] Analyze multi-agent compatibility
  - Owner: [Engineering Lead]
  - Target: ≥80% cross-agent compatibility without modification
  - Deliverable: `research-artifacts/analysis/multi-agent-compatibility.md`
  - Due: Week 3

### Phase 2 Checkpoint & Decision Gate

- **T2.15** Phase 2 exit review + go/kill/pivot decision
  - Decision: Does hero workflow meet TTFW target and pass satisfaction threshold?
  - Go: ≥75% completion, satisfaction ≥4/5, ≥80% agent compatibility → advance to Phase 3
  - Pivot: Workflow works for segment 2 not 1 → narrow focus
  - No-Go: Core value unclear; redesign needed → extend Phase 2
  - Deliverable: `research-artifacts/decisions/phase-2-decision.md`
  - Due: End of week 3

---

## Phase 3: Channel & Acquisition Testing

**Objective**: Validate repeatable acquisition path for highest-PMF segment

**Duration**: 4 weeks | **Owner**: [Growth Lead]

**Exit Criteria**: Activation 15%+ on leading channel; clear CAC + retention path

### Task Group 1: Channel Prep

- **T3.1** Design launch campaign for channel 1 (e.g., Product Hunt)
  - Owner: [Growth Lead]
  - Content: Title, tagline, deck, demo video, hunter strategy
  - Deliverable: Launch plan
  - Due: Week 1

- **T3.2** Design launch campaign for channel 2 (e.g., Twitter launch thread)
  - Owner: [Content/Growth Lead]
  - Content: Thread outline, timing, engagement plan
  - Deliverable: Tweet draft
  - Due: Week 1

- **T3.3** Design launch campaign for channel 3 (e.g., community outreach)
  - Owner: [Growth Lead]
  - Content: Community selection, moderation approach, onboarding flow
  - Deliverable: Community engagement plan
  - Due: Week 1

### Task Group 2: Campaign Execution

- [P] **T3.4** Execute channel 1 launch
  - Owner: [Growth Lead]
  - Deliverable: Campaign live; daily tracking active
  - Due: Week 1-2

- [P] **T3.5** Execute channel 2 launch
  - Owner: [Content Lead]
  - Deliverable: Campaign live; daily tracking active
  - Due: Week 1-2

- [P] **T3.6** Execute channel 3 outreach
  - Owner: [Growth Lead]
  - Deliverable: Community engaged; early adopters on-boarded
  - Due: Week 1-2

### Task Group 3: Metrics & Analysis

- **T3.7** Instrument and track activation funnel per channel
  - Owner: [Analytics/Product]
  - Metrics: Signups, hero workflow start, completion, satisfaction
  - Deliverable: Dashboard live
  - Due: Week 1

- [P] **T3.8** Daily check-in: channel performance (weeks 1-4)
  - Owner: [Growth Lead]
  - Type: Ongoing monitoring
  - Deliverable: Daily metrics snapshot in Slack/shared doc
  - Due: Daily

- **T3.9** Weekly analysis: which channel + segment performing best?
  - Owner: [Growth + Product]
  - Deliverable: Weekly summary with performance ranking
  - Due: Weekly (end of each week)

### Task Group 4: Quick Growth Experiments

- **T3.10** [RQ6] Test copy variation on best-performing channel (week 2-3)
  - Owner: [Growth Lead]
  - Hypothesis: Better headline/tagline increases activation
  - Deliverable: A/B test results at `research-artifacts/experiments/copy-test.md`
  - Due: Week 3

- **T3.11** [RQ6] Test onboarding flow improvement (week 3)
  - Owner: [Product/Design]
  - Hypothesis: Clearer first-time-user guidance improves hero workflow start rate
  - Deliverable: Onboarding variant + metrics at `research-artifacts/experiments/onboarding-test.md`
  - Due: Week 3

### Task Group 5: Network Effects Measurement (if marketplace)

- **T3.12** [RQ5] Track kit submission → user signup correlation
  - Owner: [Analytics]
  - Measure: Each kit submission → user signups within 7 days
  - Deliverable: Scatter plot + R² calculation
  - Due: Week 3-4

- **T3.13** [RQ5] Track cross-side conversion (users → creators)
  - Owner: [Analytics]
  - Measure: % of users who submit a kit within 30 days
  - Target: ≥10% cross-side conversion
  - Deliverable: `research-artifacts/analysis/network-effects.md`
  - Due: Week 4

### Phase 3 Checkpoint & Decision Gate

- **T3.14** [RQ5][RQ6] Phase 3 exit review: go-to-market validation
  - Decision: Do we have a repeatable, scalable acquisition path?
  - Scale: Activation ≥15%, D7 retention ≥30%, clear channel winner, R² > 0.4 (if marketplace) → ready to grow
  - Optimize: Metrics good but not great → optimize campaigns before broad scale
  - Pivot: Weak across channels → revisit hero workflow or positioning
  - No-Go: Activation <10% → need fundamental value rework
  - Deliverable: `research-artifacts/decisions/phase-3-decision.md`
  - Due: End of week 4

---

## Phase 4: Research Archive (Required)

**Objective**: Preserve research artifacts for future reference and stakeholder communication

**Duration**: 1 week post-Phase 3 | **Owner**: [Research Lead]

### Task Group 1: Archive & Documentation

- **T4.1** De-identify interview transcripts
  - Owner: [Research Lead]
  - Remove: Names, company info, identifying details
  - Deliverable: `research-artifacts/transcripts-de-identified/`
  - Due: Day 2

- **T4.2** Compile quote library by hypothesis/persona
  - Owner: [Research Lead]
  - Organize: Verbatim quotes tagged by RQ#, persona, insight type
  - Deliverable: `research-artifacts/analysis/quote-library.md`
  - Due: Day 3

- **T4.3** Create internal briefing document
  - Owner: [Product Lead]
  - Content: 1-page executive summary + 5-10 page detailed findings
  - Deliverable: `research-artifacts/stakeholder-review/internal-briefing.md`
  - Due: Day 5

- **T4.4** Document lessons learned for methodology improvement
  - Owner: [Research Lead]
  - Content: What worked, what didn't, recommendations for next cycle
  - Deliverable: `research-artifacts/lessons-learned.md`
  - Due: Day 7

---

## Cross-Phase: Continuous Rituals

### Weekly PMF Review (Every Monday)

- **T0.1** Run weekly PMF sync (45 min)
  - Owner: [Product Lead]
  - Attendees: Product, Growth, Design, Community
  - Agenda:
    1. **Metrics Review** (10 min): Phase-specific numbers
    2. **Learnings** (15 min): Quotes, patterns, surprises
    3. **Blockers** (10 min): Issues slowing progress
    4. **Decisions** (5 min): Pivot signals? Adjust questions?
    5. **Next Week** (5 min): Task assignments, PDCA priorities
  - Deliverable: Updated Notion dashboard + documented decisions
  - Recurrence: Every Monday

### Document Management

- **T0.2** Maintain running research synthesis doc
  - Owner: [Product Lead]
  - Content: Key quotes, persona updates, JTBD evidence, evolving hypotheses
  - Deliverable: `research-artifacts/synthesis.md` (updated weekly)
  - Recurrence: Ongoing

- **T0.3** Create phase-end summary (after each phase)
  - Owner: [Product Lead]
  - Content: What did we learn? What changed? Go/pivot/kill decision?
  - Deliverable: `research-artifacts/phase-X-summary.md`
  - Recurrence: Every 3-4 weeks

---

## Parallel Execution Map

**Week 1-2** (Concurrent execution):
- Recruitment (T1.1-T1.3): All parallel
- Interviews batch 1 (T1.4): Parallel with recruitment completion

**Week 3-4** (Concurrent execution):
- Interviews batch 2-3 (T1.5-T1.6)
- Synthesis begins (T1.7-T1.9): Parallel with final interviews

**Week 5-7** (Phase 2 - Concurrent):
- Usability test prep (T2.1-T2.3): Parallel
- Multi-agent setup (T2.10-T2.11): Parallel with prep
- Usability tests (T2.4-T2.6): Batch execution
- Multi-agent tests (T2.12-T2.13): Parallel with usability tests

**Week 8-11** (Phase 3 - Concurrent):
- Channel campaigns (T3.4-T3.6): All parallel
- Analytics tracking (T3.7-T3.9): Parallel with campaigns
- Growth experiments (T3.10-T3.11): Week 10-11
- Network effects (T3.12-T3.13): Week 10-11

**Week 12** (Phase 4):
- Archive tasks (T4.1-T4.4): Sequential

---

## Dependencies & Critical Path

**Phase Dependencies**:
- **Phase 1** MUST complete before Phase 2 (need validated personas + JTBD)
- **Phase 2** MUST show successful hero workflow before Phase 3 (otherwise channel testing meaningless)
- **Phase 3** validates go-to-market; informs scaling decisions
- **Phase 4** archives learnings for future reference

**Critical Path Tasks**:
- T1.2, T1.3 (Participant recruitment) — 2-week lead time drives timeline
- T2.1-T2.3 (Usability prep) — Blocks all usability tests
- T2.10-T2.11 (Agent setup) — Blocks multi-agent testing
- T3.7 (Analytics instrumentation) — Blocks all channel tracking

**Total Duration**: 12 weeks (4+3+4+1) for full discovery cycle
**Critical Path Indicator**: Participant recruitment (T1.2, T1.3) + agent setup (T2.10-T2.11) drive timeline

---

## Success Metrics Summary

By end of all phases, we will have:

| Metric | Target | Research Question |
|--------|--------|-------------------|
| Persona pain frequency | ≥70% report 2+ hrs/week | RQ1 |
| Willingness-to-try | ≥60% mention actively searching | RQ1 |
| Willingness-to-pay | ≥40% indicate $5-20/mo | RQ3 |
| Hero workflow completion | ≥75% complete end-to-end | RQ2 |
| TTFW | < [target] time | RQ2 |
| User satisfaction | ≥4.0/5.0 avg | RQ2 |
| Multi-agent compatibility | ≥80% cross-agent success | RQ4 |
| Channel activation | ≥15% on best channel | RQ6 |
| D7 retention | ≥30% on best channel | RQ6 |
| Network effects (if marketplace) | R² > 0.4 | RQ5 |
| Cross-side conversion (if marketplace) | ≥10% | RQ5 |

✅ **PMF Decision**: GO/SCALE, PIVOT, or NO-GO with confidence and data

---

## Next Steps

1. **Run `/pmfkit.implement`** to begin executing Phase 1 tasks
2. **At phase transitions**: Run `/pmfkit.optimize` to refine hypotheses
3. **After Phase 4**: Review lessons learned; plan next discovery cycle or scaling
