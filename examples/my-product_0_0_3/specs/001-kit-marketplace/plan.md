# agentii-kit Marketplace: PMF Research Plan

**Feature Branch**: `001-kit-marketplace`
**Created**: 2025-12-04
**Status**: Draft
**Discovery Phase**: Phase 0-1 Planning (Problem & Persona Validation)

---

## Research Context *(mandatory)*

**Platform**: Open-source marketplace for AI-agent-ready spec-kit job kits across domains (Marketing, Legal, Product, Finance, Education)

**Core Hypotheses**:
- Domain experts have acute pain sharing knowledge; they're motivated by recognition, not revenue
- Junior practitioners waste 5-20 hours/project repeating workflows; they'd adopt vetted expert kits
- AI agents + GitHub adoption create optimal timing for such a marketplace
- Product Hunt + GitHub launch can drive early adoption among spec-kit enthusiasts and AI agent communities

### Primary Research Questions

**Question 1**: "Do domain experts actually experience pain sharing expertise? Are they motivated by recognition or revenue?"
- Hypothesis: ≥70% report monthly+ pain; ≥80% prefer free platform with visibility over paid model
- Success threshold: Validated via interviews (N=12-15 creators) + Gumroad vs. GitHub analysis
- Evidence source: In-depth interviews (60 min, creators); creator motivation survey; GitHub trends

**Question 2**: "Do practitioners waste time repeating processes? Would they adopt expert kits?"
- Hypothesis: ≥75% report monthly+ workflow pain; ≥80% would use free kit if saved 5+ hours
- Success threshold: Validated via interviews (N=12-15 practitioners) + Notion marketplace analysis
- Evidence source: In-depth interviews (45 min, practitioners); template marketplace survey (N=100-200)

**Question 3**: "Can kit creators publish in <30 min? Can kit users go discovery→execution in <15 min?"
- Hypothesis: ≥70% creators complete in <30 min with satisfaction ≥4/5; ≥75% users complete in <15 min
- Success threshold: Validated via usability tests (creator + user flows)
- Evidence source: Moderated usability testing (5-8 creators, 8-10 users); time measurement + satisfaction surveys

**Question 4**: "Will Product Hunt + GitHub audience adopt agentii-kit? Do early adopters match personas?"
- Hypothesis: ≥70% of community influencers willing to share; ≥80% of beta testers rate ≥4/5
- Success threshold: Pre-launch community outreach + beta feedback analysis
- Evidence source: Influencer interviews (N=10-15); beta user surveys + referral tracking

### Research Phases & Exit Criteria

Research progresses through **PDCA cycles** over **4 weeks**:

**Week 1-2 (Plan → Do)**: Recruit participants; conduct creator + practitioner interviews; market signal surveys
**Week 2-3 (Do → Check)**: Usability tests (creator and user workflows); multi-agent compatibility testing; analyze feedback
**Week 4 (Check → Act)**: Compile findings; make Go/No-Go/Pivot decision for Phase 2; prepare Phase 2 (Workflow Validation) planning

---

## Constitution Check *(mandatory)*

Verify alignment with agentii-kit principles (/.pmf/memory/constitution.md):

- [x] **Kit-First Specification**: All research questions operationalize spec.md hypotheses (personas, JTBDs, hero workflows, success metrics)
- [x] **Customer-Evidence-Driven**: Direct evidence via interviews, behavior tests, not assumptions; trace all research to real customer signals
- [x] **Iterative Validation**: PDCA gates weekly; explicit go/no-go/pivot criteria for each hypothesis block
- [x] **Minimal Viable Process**: Qualitative interviews before quantitative surveys; manual usability tests before automated analytics
- [x] **Multi-Agent Interoperability**: H4.1 research validates Claude Code + Cursor + Copilot compatibility

---

## Phase 1: Problem & Persona Validation

**Goal**: Confirm domain expert creators and junior practitioner users both exist, face real pain, and would adopt agentii-kit

**Duration**: 4 weeks | **Owner**: [Product Lead] + [Research Lead]

**Research Activities**:

1. **Creator Interviews** (N=12-15, 60 min each):
   - Validate: H1.1 (pain sharing knowledge), H1.2 (motivation), and gather context for H1.3 (kit publication feasibility)
   - Recruitment: LinkedIn outreach to PMs, Legal Counsel, Marketing Directors, Financial Analysts, Educators
   - See: `research-instruments.md` → Interview Protocol 1

2. **Practitioner Interviews** (N=12-15, 45 min each):
   - Validate: H2.1 (pain discovering/adopting workflows), H2.2 (willingness to use kits), and gather context for H2.3 (user workflow feasibility)
   - Recruitment: LinkedIn, Reddit (r/productivity, r/startups), career Discord, career forums
   - See: `research-instruments.md` → Interview Protocol 2

3. **Template Marketplace Survey** (N=100-200, ~3 min):
   - Validate: H3.1 (existing demand for template marketplaces), H5.1 (willingness to switch to agentii-kit)
   - Recruitment: Notion template marketplace, Gumroad communities, Zapier forums
   - See: `research-instruments.md` → Survey Template

4. **Creator Usability Test** (N=5-8 moderated sessions, 45 min each):
   - Validate: H1.3 (kit creator can publish in <30 min)
   - See: `research-instruments.md` → Usability Test Protocol 1

5. **User Usability Test** (N=8-10 moderated sessions, 35 min each):
   - Validate: H2.3 (kit user can discover→fork→customize→execute in <15 min)
   - See: `research-instruments.md` → Usability Test Protocol 2

6. **Multi-Agent Technical Validation** (concurrent):
   - Validate: H4.1 (kits work across Claude Code, Cursor, Copilot)
   - Test 2 reference kits (PM-Kit, Marketing-Kit) on 2+ agents with 5-10 real users per agent
   - See: `research-instruments.md` → Technical setup section

7. **Influencer / Community Leader Outreach** (N=10-15 interviews, 30 min each):
   - Validate: H5.1 (Product Hunt + GitHub audience), H5.2 (early adopters match personas)
   - Pre-launch community alignment; gauge willingness to share on launch day
   - Communities: spec-kit Reddit, Cursor / Claude Code Discord, ProductTank, r/productivity, r/startups

**Deliverables**:
- Creator JTBD validation summary (pain, motivation, quote highlights)
- User JTBD validation summary (pain, adoption drivers, quote highlights)
- Creator workflow usability report (friction points, time measurement, satisfaction scores)
- User workflow usability report (friction points, time measurement, NPS)
- Multi-agent compatibility assessment (agents supported, known issues, workarounds)
- Template marketplace demand analysis (existing users, switching interest, feature gaps)
- Community readiness assessment (influencer enthusiasm, likely launch day activity)
- Compiled go/no-go/pivot decision matrix (see: `validation-checkpoints.md`)

**Weekly PDCA Rhythm**:

| Week | Do | Check | Act |
|------|----|----|-----|
| **Week 1** | Recruit participants (N=24 interviews target 70% recruited); finalize interview guides | 70% recruited? | Activate backup recruitment if needed |
| **Week 2** | Conduct interviews (12-15 creator + 12-15 practitioner); begin usability tests | Interview saturation reached? Patterns clear? | Adjust usability test scenarios based on interview learnings |
| **Week 3** | Complete usability tests (creator + user); begin multi-agent testing; send marketplace survey | Usability friction points identified? Which agents compatible? | Prioritize refinements for Phase 2 |
| **Week 4** | Analyze all findings; score against hypothesis go/no-go thresholds; prepare phase summary | Do we meet Go criteria for all 5 hypothesis clusters? | Recommend Phase 2 scope (Full launch? Segment focus? Platform redesign?) |

**Phase 1 Exit Criteria** (See `validation-checkpoints.md` for detailed thresholds):

- [ ] **GO to Phase 2**: Creator JTBD + User JTBD + Hero Workflow Feasibility all GO; Market signals GO or PIVOT acceptable
- [ ] **PIVOT to Phase 1.5**: 1-2 hypothesis clusters PIVOT (close but need refinement); others GO → Refine + re-test
- [ ] **NO-GO / Strategic Hold**: ≥2 hypothesis clusters NO-GO → Deep-dive on failure signals; consider platform redesign

**Successful Phase 1 Output**:
- Executive summary (1 page): Personas validated? JTBDs real? Workflows feasible? Go/No-Go/Pivot decision + rationale
- Detailed findings report (5-10 pages): Creator insights, User insights, workflow friction, market readiness, multi-agent assessment
- Research artifacts: Interview transcripts (de-identified), usability test videos/notes, survey results, quote library
- Participant pool tracked for Phase 2 (willingness to beta test)
- Updated persona definitions (any adjustments from spec.md?)
- Recommended adjustments to Phase 2 scope based on Phase 1 learnings

---

## Phase 2: Hero Workflow Validation & Market Testing (Post-Phase 1)

**Goal**: Scale-test hero workflows; begin channel & retention tracking; prepare for Product Hunt launch

**Duration**: 3-4 weeks (post-Phase 1 exit decision) | **Owner**: [Product Lead] + [Growth Lead]

**Scope** (contingent on Phase 1 results):
- If Phase 1 GO: Run 50-100 user workflow tests; soft-launch to 2-3 channels; measure D7 retention
- If Phase 1 PIVOT: Run refinement iterations + limited re-testing (10-15 users)
- If Phase 1 NO-GO: Hold; deep-dive on failure signals; strategic reassessment

**Planned Activities** (Phase 1 GO scenario):
1. **Scale Workflow Testing** (N=50-100): Expand usability test pool; measure activation, satisfaction, NPS at scale
2. **Retention Tracking**: First 7-30 days post-hero workflow; track kit re-use, community engagement, referral activity
3. **Soft-Launch Beta Groups** (N=200-500): Limited release to high-interest communities (spec-kit, Cursor, Claude Code)
4. **Channel Testing** (2-3 channels): Product Hunt, GitHub Trending, Twitter launch strategies; measure CAC, activation, retention by channel

**Phase 2 Success Criteria**:
- ≥75% of tested users complete hero workflow; satisfaction ≥4/5; NPS ≥30
- D7 retention ≥25% from soft-launch beta
- Clear winner channel identified (2x+ performance vs. 2nd place)

**Successful Phase 2 Output**:
- Scale workflow testing report
- Retention cohort analysis
- Channel performance summary + recommended launch strategy
- Go/No-Go decision for public launch (Phase 3)
- Updated product roadmap (Phase 2 learnings → Phase 3 launch features)

---

## Phase 3: Channel & Acquisition Testing

**Goal**: Validate repeatable, scalable acquisition path; prepare for 10K+ user scale

**Duration**: 4-6 weeks (post-Phase 2, contingent on Phase 1+2 GO) | **Owner**: [Growth Lead]

**Planned Activities**:
1. **Product Hunt Launch** (with 5-7 seeded kits): Measure upvotes, maker engagement, signups, D1/D7 retention
2. **GitHub Trending**: Measure GitHub stars, forks, contributors; track by kit domain
3. **Twitter / Social**: Creator interviews, demo videos, problem-solution narratives; track amplification
4. **Community Launches** (spec-kit, Cursor, Claude Code, r/productivity, ProductTank): Soft activations → full community partnerships
5. **Content + SEO**: Blog posts on "Why agentii-kit," "How to create a kit," "Kit gallery"; organic discovery tracking

**Metrics Tracked**:
- CAC by channel; CAC payback period
- Signup → hero workflow activation rate
- D1, D7, D30 retention by channel + persona
- Kit fork rate; community contribution rate (PRs, discussions)
- NPS from early adopters; willingness to refer

**Phase 3 Success Criteria**:
- ≥200 total signups; ≥150 complete hero workflow
- ≥25% D7 retention from cohort
- CAC < $10 (if any paid spend); strong viral coefficient (1 user → 0.3+ new users)
- Clear channel winner (e.g., "Product Hunt outperforms GitHub 3x; Twitter underperforms")

---

## Validation Checkpoints & Weekly Rituals

### Weekly PMF Review (Every Monday, 60 min)

**Attendees**: Product, Research, Growth, Engineering, Community Lead

**Agenda**:
1. **Hypothesis Dashboard**: Which hypotheses moved this week? (Green/yellow/red status)
2. **Key Learnings**: 2-3 biggest surprises or insights from research
3. **Blockers**: What's slowing progress? Resource needs?
4. **Next Week PDCA**: Do/Check/Act planning

**Output**: Updated research roadmap; any escalations for stakeholders

### Phase-End Review (Week 4, Week 8, Week 12)

**Decision Ritual**:
1. **Score Against Exit Criteria**: Do we meet thresholds? (Go/No-Go/Pivot)
2. **Stakeholder Review**: Present findings + recommendation to leadership
3. **Decision**: Approved to advance to next phase?
4. **Plan Phase N+1**: If GO, begin planning next phase

---

## Research Governance & Tracking

### Research Question Traceability

All research is directly traceable to spec.md hypotheses:

| Spec Section | Hypothesis | Research Questions | Instruments | Timeline |
|--------------|------------|-------------------|-------------|----------|
| Creator JTBD | H1.1-1.3 | Q1, Q3 (creator workflow) | Interviews (Protocol 1), Usability Tests (Protocol 1) | Week 1-3 |
| User JTBD | H2.1-2.3 | Q2, Q3 (user workflow) | Interviews (Protocol 2), Usability Tests (Protocol 2) | Week 1-3 |
| Market Signals | H3.1-3.2, H5.1-5.2 | Q4, Market surveys | Community outreach, Marketplace survey | Week 1-2 |
| Technical Feasibility | H4.1 | Multi-agent testing | Technical validation sessions | Week 2-3 |
| Success Metrics | All | Post-research instrumentation | Analytics setup, retention tracking | Phase 2+ |

### Data Management

- **Interview recordings & transcripts**: Stored securely; de-identified in reports; archived for 12 months
- **Usability test videos**: Key clips extracted; stored with participant consent; deleted after analysis
- **Quantitative data**: Spreadsheets with analysis; confidence intervals tracked
- **Quotes library**: Compiled for marketing, product updates, and stakeholder comms

---

## Success Criteria Summary

| Phase | Hypothesis | Success Threshold | No-Go Threshold | Decision Authority |
|-------|-----------|-------------------|-----------------|-------------------|
| **Phase 1** | Creator JTBD real | ≥70% pain; ≥80% recognition motivation | <50% pain | [Product] + [Stakeholders] |
| **Phase 1** | User JTBD real | ≥75% pain; ≥80% willingness-to-adopt | <50% pain | [Product] + [Stakeholders] |
| **Phase 1** | Creator workflow feasible | ≥70% complete <30 min; satisfaction ≥4/5 | <50% complete | [Product] + [Design] |
| **Phase 1** | User workflow feasible | ≥75% complete <15 min; NPS ≥30 | <50% complete | [Product] + [Design] |
| **Phase 1** | Market ready | ≥70% influencer share; ≥80% beta enthusiasm | <40% influencer interest | [Product] + [Growth] |
| **Phase 2** | Scale workflows | ≥75% complete; satisfaction ≥4/5 | <60% complete | [Product] + [Growth] |
| **Phase 2** | Retention acceptable | D7 ≥25% from beta | D7 <15% | [Product] + [Growth] |
| **Phase 3** | Channel validation | Clear winner (2x+ vs 2nd); CAC < $10 | No winner identified | [Growth] + [Stakeholders] |

---

## Artifacts Generated

### Phase 1 Research Artifacts

- ✅ `research-questions.md`: All 5 hypothesis clusters operationalized into testable research questions
- ✅ `research-instruments.md`: Detailed protocols for all research activities (interviews, surveys, usability tests)
- ✅ `validation-checkpoints.md`: PDCA gates, go/no-go criteria, and decision frameworks for each hypothesis block
- ✅ `plan.md` (this file): Comprehensive research plan covering Phases 1-3

### Supporting Files

- `spec.md`: Original feature specification with personas, JTBDs, hero workflows
- `.pmf/memory/constitution.md`: Platform principles (Kit-First Specification, Customer-Evidence-Driven, etc.)
- `CLAUDE.md`: Agent context for Claude Code; includes research methodology

---

## Next Steps

**Immediately** (This week):
1. ✅ Review `research-questions.md` with stakeholders; confirm hypothesis prioritization
2. ✅ Review `research-instruments.md` with research team; finalize interview guides + usability test scenarios
3. ✅ Review `validation-checkpoints.md` with decision-makers; confirm go/no-go thresholds
4. ⏭️ Begin recruitment: Outreach to creator + practitioner candidates on LinkedIn, Reddit, Discord

**Week 1 (Next 7 days)**:
1. ⏭️ Activate recruitment channels; target 70% of N=24 interview slots filled
2. ⏭️ Finalize Claude Code / Cursor setup for usability testing
3. ⏭️ Prepare usability test scenarios with product team
4. ⏭️ Send marketplace survey to Notion / Gumroad communities

**Week 2-4 (Research Execution)**:
1. ⏭️ Run interviews 2-3x per week (creator + practitioner)
2. ⏭️ Conduct usability tests as participants are recruited
3. ⏭️ Begin multi-agent technical validation (concurrent)
4. ⏭️ Monitor marketplace survey responses

**Week 4 (Phase 1 Close)**:
1. ⏭️ Synthesize all findings
2. ⏭️ Score against go/no-go thresholds
3. ⏭️ Present Phase 1 findings to stakeholders
4. ⏭️ Plan Phase 2 scope (GO scenario) or escalate (PIVOT/NO-GO scenario)
