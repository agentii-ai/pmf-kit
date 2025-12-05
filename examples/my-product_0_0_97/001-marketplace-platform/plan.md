# PMF Research Plan: Agentii-Kit Marketplace

**Feature Branch**: `001-marketplace-platform`
**Created**: 2025-12-05
**Status**: Draft
**Discovery Phase**: Phase 0 - Foundation (Research Planning Complete)
**Plan Owner**: Product Lead / Research Lead

---

## Research Context *(mandatory)*

This research plan operationalizes all hypotheses from the PMF spec (`spec.md`) into a systematic validation strategy. We will answer 9 core research questions across 3 phases (15 weeks total) using qualitative interviews, usability tests, technical validation, and behavioral analytics.

**Core Hypothesis**: Professionals across domains (marketing, PM, legal) waste 2-3 hours/week reinventing workflows, and a GitHub-native marketplace of AI-agent-ready job kits can solve this pain with ≥30% D7 retention and network effects (R² > 0.4).

**Target Personas**:
1. **Kit Creators** (Sarah, Marketing Ops Lead): Want to share reusable workflows, reduce duplicate questions
2. **Kit Users** (Marcus, Product Manager): Need structured templates to accelerate work
3. **Startup Founders** (Lisa, Technical Founder): Need playbooks for non-technical tasks

---

### Primary Research Questions

**Question 1 (P1)**: Do Kit Creator and Kit User personas have real, frequent pain requiring our solution?
- **Hypothesis**: ≥70% of target personas waste 2-3 hours/week reinventing workflows and actively search for templates
- **Success threshold**: ≥70% report pain ≥2 hours/week; ≥50% actively search for templates
- **Evidence source**: In-depth interviews (45-60 min, N=20: 10 creators + 10 users)
- **See**: `research-questions.md` → RQ1 | `research-instruments.md` → Interview Guide #1

**Question 2 (P1)**: Can Hero Workflow 1 (Discover and Fork a Kit) be completed in <10 minutes by non-developers?
- **Hypothesis**: ≥75% of non-developers can complete workflow in ≤10 min with ≥4/5 satisfaction
- **Success threshold**: ≥75% complete in ≤10 min; ≥70% rate ≥4/5 stars; ≥60% have "wow moment"
- **Evidence source**: Moderated usability tests (N=10: 5 Kit Users + 5 Kit Creators)
- **See**: `research-questions.md` → RQ2 | `research-instruments.md` → Usability Test Protocol #1

**Question 3 (P1)**: Which persona has highest retention and willingness-to-pay?
- **Hypothesis**: Kit Users have higher retention than Kit Creators (immediate time-saving value)
- **Success threshold**: Identify 1 persona with D7 retention ≥30% and D30 ≥20%
- **Evidence source**: Phase 1 interviews (WTP probes) + Phase 3 beta (behavioral tracking, N=50+)
- **See**: `research-questions.md` → RQ3 | `research-instruments.md` → Survey Template #1

**Question 4 (P1)**: Can we achieve ≥80% cross-agent compatibility for kits?
- **Hypothesis**: Kits work across Claude Code + Cursor with ≥80% compatibility
- **Success threshold**: ≥80% of tested kits (N=10) work with Claude Code + Cursor
- **Evidence source**: Technical validation (N=10 seed kits × 3 agents)
- **See**: `research-questions.md` → RQ4 | `research-instruments.md` → Multi-Agent Compatibility Test #1

**Question 5 (P2)**: Do users prefer curated collections or open browse for kit discovery?
- **Hypothesis**: Non-developers prefer curated; developers prefer browse/search
- **Success threshold**: ≥60% preference for one discovery method OR clear persona split
- **Evidence source**: Usability tests (N=10, A/B test discovery UX) + Phase 3 behavioral analytics
- **See**: `research-questions.md` → RQ5 | `research-instruments.md` → Usability Test Protocol #1

**Question 6 (P2)**: Will supply-side (Kit Creators) materialize without incentives?
- **Hypothesis**: We can recruit 10-15 early creators to seed marketplace with 20-30 kits
- **Success threshold**: ≥10 creators commit to publishing; ≥70% actually publish
- **Evidence source**: Direct outreach (N=30 targets) + interviews (N=10 creators)
- **See**: `research-questions.md` → RQ6 | `research-instruments.md` → Interview Guide #1 (Creator section)

**Question 7 (P3)**: Is creator reputation scoring necessary in MVP?
- **Hypothesis**: Reputation scoring can be deferred; manual curation sufficient for MVP
- **Success threshold**: <40% of users mention reputation as important trust signal → Defer to post-PMF
- **Evidence source**: Usability tests (trust signals experiment, N=10) + interviews (N=20)
- **See**: `research-questions.md` → RQ7 | `research-instruments.md` → Usability Test Protocol #1

**Question 8 (P3)**: Do network effects exist? (Does more supply drive more demand?)
- **Hypothesis**: R² > 0.4 correlation between kit count and user signups; ≥10% cross-side conversion
- **Success threshold**: R² > 0.4 AND ≥10% users become creators within 90 days
- **Evidence source**: Phase 3 beta behavioral analytics (N=50+ users, 20-30 kits, 6-8 weeks)
- **See**: `research-questions.md` → RQ8

**Question 9 (Ongoing)**: Which distribution channel delivers highest-quality users?
- **Hypothesis**: Product Hunt drives volume; communities (Twitter, Reddit) drive quality (D7 retention)
- **Success threshold**: Identify 1-2 channels with activation ≥15% AND D7 retention ≥30%
- **Evidence source**: Multi-channel launch (Product Hunt, Twitter, Reddit, GitHub, SEO) + UTM tracking
- **See**: `research-questions.md` → RQ9 | `research-instruments.md` → Experiment Protocol #1

---

### Research Phases & Exit Criteria

Research progresses through PDCA cycles (Plan → Do → Check → Act) at 4-week, 3-week, and 6-8-week intervals.

**Phase 1 – Problem & Persona Validation** (4 weeks):
- **Goal**: Validate personas have real, frequent pain; recruit creators; confirm cross-agent compatibility
- **Activities**: 20 interviews (10 creators + 10 users), 30 creator outreach, 10 seed kits × 3 agents technical test
- **Exit Criteria**: ≥70% personas report pain ≥2 hrs/week; ≥10 creators recruited; ≥80% cross-agent compatibility
- **Decision Gate**: GO (advance to Phase 2) / PIVOT (adjust personas/thresholds) / KILL (insufficient pain)
- **See**: `validation-checkpoints.md` → Phase 1 → Phase 2 Gate

**Phase 2 – Hero Workflow Validation** (3 weeks):
- **Goal**: Validate Hero Workflow 1 achievable in <10 min by non-developers; determine discovery UX preference
- **Activities**: 10 usability tests (5 Kit Users + 5 Kit Creators), A/B test discovery UX, trust signals experiment
- **Exit Criteria**: ≥75% complete workflow in ≤10 min with ≥4/5 satisfaction; discovery UX preference clear
- **Decision Gate**: GO (launch beta) / PIVOT (redesign UX friction) / KILL (TTFW unachievable)
- **See**: `validation-checkpoints.md` → Phase 2 → Phase 3 Gate

**Phase 3 – Network Effects & Channel Validation** (6-8 weeks):
- **Goal**: Validate network effects (R² > 0.4); identify high-quality distribution channels; measure PMF metrics
- **Activities**: Launch beta (N=50+ users), seed 20-30 kits, multi-channel launch (Product Hunt, Twitter, Reddit, GitHub)
- **Exit Criteria**: R² > 0.4, ≥10% cross-side conversion, D7 ≥30%, NPS ≥50, Sean Ellis ≥40%
- **Decision Gate**: SCALE (invest in growth) / ITERATE (optimize UX/positioning) / PIVOT (major change)
- **See**: `validation-checkpoints.md` → Phase 3 → Post-PMF Gate

---

## Constitution Check *(mandatory)*

Verify alignment with Agentii-Kit constitution principles (`.pmf/memory/constitution.md`):

- [x] **Principle I (Marketplace-First Thinking)**: Research questions cover both supply (creators) and demand (users) perspectives (RQ1, RQ3, RQ6, RQ8)
- [x] **Principle II (Kit Quality Standards)**: Technical validation confirms 4-file structure, README, multi-agent compatibility (RQ4)
- [x] **Principle III (Provider Enablement)**: Creator recruitment and submission workflow validation planned (RQ6, Hero Workflow 2)
- [x] **Principle IV (Discovery & Curation)**: Discovery UX preference testing included (RQ5)
- [x] **Principle V (GitHub-Native Architecture)**: Technical validation confirms GitHub fork workflow (RQ2, RQ4)
- [x] **Principle VI (Multi-Agent Compatibility)**: Cross-agent compatibility testing with ≥80% threshold (RQ4)
- [x] **Principle VII ("Fork to Work" Philosophy)**: Hero Workflow 1 validates "discover → fork → execute" flow (RQ2)
- [x] **Principle VIII (Spec-Driven Workflow Consistency)**: All kits enforce 4-file architecture in technical validation
- [x] **Principle IX (Namespace Isolation)**: Uses `agentiikits.*` commands (validated in technical tests)
- [x] **Principle X (Accessibility & Inclusivity)**: Non-developer usability testing confirms accessibility (RQ2)

---

## Budget & Resources *(mandatory)*

### Participant Incentives

| Activity | Participants | Incentive | Total |
|----------|--------------|-----------|-------|
| Phase 1 Interviews | N=20 | $50/person | $1,000 |
| Phase 2 Usability Tests | N=10 | $50/person | $500 |
| Phase 3 Beta Testers | N=50+ | Early access | $0 |
| **Total Budget** | | | **$1,500** |

### Tools & Platforms

- **Interviews**: Zoom (video), Calendly (scheduling), Notion/Airtable (synthesis)
- **Usability Tests**: Zoom (screen share), Figma (mockups), Loom (recordings)
- **Technical Validation**: GitHub (repos), Claude Code, Cursor, Copilot (agents)
- **Analytics**: Vercel Analytics (user behavior), GitHub API (kit metadata), internal database (forks/submissions)
- **Surveys**: Typeform or Google Forms (NPS, Sean Ellis test, WTP surveys)

### Team Allocation

| Role | Phase 1 (4 weeks) | Phase 2 (3 weeks) | Phase 3 (6-8 weeks) |
|------|-------------------|-------------------|---------------------|
| **Product Lead** | 50% (interviews, synthesis) | 50% (usability tests, decision gates) | 30% (metrics monitoring, PDCA reviews) |
| **Research Lead** | 80% (interviews, recruitment, analysis) | 80% (usability tests, analysis) | 50% (behavioral analysis, channel tracking) |
| **Eng Lead** | 30% (technical validation, instrumentation) | 20% (prototype support) | 40% (beta support, instrumentation) |
| **Design Lead** | 20% (interview support) | 60% (usability tests, UX redesign) | 20% (UX iteration based on feedback) |

---

## Risk Mitigation *(mandatory)*

| Risk | Impact | Mitigation | Fallback |
|------|--------|------------|----------|
| **Participant recruitment fails** (<15 interviews) | High | Increase incentive $50→$75; expand sourcing channels; snowball sampling | Extend Phase 1 by 2 weeks; accept N=15 if patterns saturate |
| **Creator recruitment fails** (<10 creators) | High | Offer stronger incentives (early access, featured placement); recruit from different channels (LinkedIn, Discord) | Team creates all seed kits; defer community contribution to post-MVP |
| **Cross-agent compatibility <80%** | High | Document workarounds aggressively; lower threshold to 70%; focus on Claude Code + Cursor only | Update constitution; build MVP for Claude Code only (single-agent focus) |
| **Hero Workflow 1 TTFW >10 min for non-devs** | High | Redesign friction points (GitHub fork, template customization); add tutorial video; simplify language | Pivot to developer-only audience; adjust personas and positioning |
| **No network effects** (R² < 0.2) | Medium | Invest in creator incentives (reputation, analytics, gamification) | Pivot to curated model (team creates all kits, no community marketplace) |
| **Low retention** (D7 <20%) | High | Run `/pmfkit.optimize` to refine UX/positioning; interview churned users; A/B test improvements | Major pivot (audience, use case, or product model) |

---

## Phase 0: Foundation & Research Design (Complete)

**Objective**: Operationalize all PMF spec hypotheses into testable research questions, instruments, and validation checkpoints

**Status**: ✅ COMPLETE

**Deliverables**:
- [x] `research-questions.md` – 9 research questions with methodologies, sample sizes, success criteria
- [x] `research-instruments.md` – Interview guides, usability test protocols, compatibility tests, survey templates, experiment protocols
- [x] `validation-checkpoints.md` – Go/kill/pivot criteria for each PDCA decision gate
- [x] Agent context updated (`CLAUDE.md`)

---

## Phase 1: Problem & Persona Validation (4 weeks)

**Objective**: Validate personas have real, frequent pain; recruit creators; confirm cross-agent compatibility

**Duration**: 4 weeks

**Team**: Product Lead (50%), Research Lead (80%), Eng Lead (30%)

### Week 1: Recruitment & Setup

**Tasks**:
- [ ] **T1.1** [P] Create screener survey (5-6 questions) → `research-artifacts/screener-survey.md`
- [ ] **T1.2** [P] Build participant recruiting list (30-40 candidates) → `research-artifacts/recruitment-list.csv`
  - Channels: Twitter #PMLife, Reddit r/ProductManagement, LinkedIn PM groups, Discord communities
- [ ] **T1.3** Recruit and schedule 20 interviews (book 3-4 per week) + 30 creator outreach targets
  - Incentive: $50/participant (budget: $1,000)
- [ ] **T1.4** [P] Prepare 10 seed kits for technical validation (marketing, PM, legal, startup, education)
- [ ] **T1.5** [P] Set up compatibility tracking spreadsheet (kit × agent → pass/fail/workaround)

### Week 2: Phase 1 Interviews Batch 1 + Technical Validation

**Tasks**:
- [ ] **T1.6** [P] Conduct interviews batch 1 (4-5 interviews) → `research-artifacts/interviews/batch-1/`
  - Duration: 45-60 min per interview
  - Protocol: See `research-instruments.md` → Interview Guide #1
  - **Checkpoint**: After batch 1, are JTBD patterns emerging? Pain frequency ≥70%?
- [ ] **T1.7** [P] Begin technical validation: Test 10 seed kits with Claude Code
  - Protocol: See `research-instruments.md` → Multi-Agent Compatibility Test #1
  - Record: Success/failure, errors, workarounds, time to complete
- [ ] **T1.8** [P] Continue creator outreach (target: 15-20 responses by end of week)

### Week 3: Phase 1 Interviews Batch 2 + Cross-Agent Testing

**Tasks**:
- [ ] **T1.9** [P] Conduct interviews batch 2 (4-5 interviews) → `research-artifacts/interviews/batch-2/`
  - Adjust questions based on batch 1 learnings
  - **Checkpoint**: Mid-phase decision — continue, pivot persona, or extend?
- [ ] **T1.10** [P] Test 10 seed kits with Cursor → Update compatibility matrix
- [ ] **T1.11** [P] Test 10 seed kits with GitHub Copilot → Final compatibility matrix
- [ ] **T1.12** Creator recruitment checkpoint: ≥10 creators committed? If not, escalate mitigation plan

### Week 4: Phase 1 Interviews Batch 3 + Synthesis

**Tasks**:
- [ ] **T1.13** [P] Conduct interviews batch 3 (remaining 8-10 interviews) → `research-artifacts/interviews/batch-3/`
- [ ] **T1.14** Create JTBD synthesis document → `research-artifacts/analysis/jtbd-synthesis.md`
  - Content: Top 3 JTBD with verbatim quotes + mention rates + frequency data
- [ ] **T1.15** Assess persona clarity + refinements → `research-artifacts/analysis/persona-validation.md`
  - Validate: Do personas match assumptions? Calculate % with ≥2 hrs/week pain
- [ ] **T1.16** Document willingness-to-pay signals → `research-artifacts/analysis/willingness-to-pay.md`
  - Analyze: Price points ($X-$Y), incumbent pain points
- [ ] **T1.17** Finalize compatibility matrix + document workarounds → `research-artifacts/analysis/cross-agent-compatibility.md`

### Phase 1 Checkpoint & Decision Gate (End of Week 4)

**Decision Authority**: Product Lead + Research Lead

**Review Criteria**: See `validation-checkpoints.md` → Phase 1 → Phase 2 Gate

- [ ] **Checkpoint 1.1**: Persona pain validation (≥70% report pain ≥2 hrs/week)
- [ ] **Checkpoint 1.2**: Creator recruitment feasibility (≥10 creators committed)
- [ ] **Checkpoint 1.3**: Cross-agent compatibility feasibility (≥80% work with Claude + Cursor)
- [ ] **Checkpoint 1.4**: Willingness-to-pay signals (≥40% indicate WTP for premium features)

**Decision**:
- **GO**: Advance to Phase 2 (usability testing)
- **PIVOT**: Re-target persona, adjust thresholds, extend timeline
- **KILL**: Insufficient pain or creator pipeline → Abandon marketplace

**Deliverables**:
- [ ] Phase 1 exit report → `research-artifacts/phase-1-exit-report.md`
- [ ] Go/pivot/kill decision document

---

## Phase 2: Hero Workflow Validation (3 weeks)

**Objective**: Validate Hero Workflow 1 achievable in <10 min by non-developers; determine discovery UX preference

**Duration**: 3 weeks

**Team**: Product Lead (50%), Research Lead (80%), Design Lead (60%), Eng Lead (20%)

**Prerequisites**: Phase 1 PASSED (personas validated, creators recruited)

### Week 5: Usability Test Prep

**Tasks**:
- [ ] **T2.1** Create marketplace homepage mockup (Figma or staging site) with sample kits
  - Variants: Curated collections (Variant A) vs. Open browse/search (Variant B)
- [ ] **T2.2** Recruit 10 usability test participants (5 Kit Users + 5 Kit Creators)
  - Screen for non-developers, GitHub account, AI agent familiarity
  - Incentive: $50/participant (budget: $500)
- [ ] **T2.3** [P] Prepare test environment: Screen recording setup, test kits, GitHub repos

### Week 6: Usability Tests Batch 1 (5 tests)

**Tasks**:
- [ ] **T2.4** [P] Conduct usability tests 1-5 → `research-artifacts/usability-tests/batch-1/`
  - Duration: 45-60 min per test
  - Protocol: See `research-instruments.md` → Usability Test Protocol #1
  - Record: Time-to-first-task, friction points, satisfaction (1-5), "wow moment" (Y/N)
- [ ] **T2.5** Mid-phase checkpoint: Are ≥75% completing workflow in ≤10 min? If not, escalate UX redesign

### Week 7: Usability Tests Batch 2 (5 tests) + Synthesis

**Tasks**:
- [ ] **T2.6** [P] Conduct usability tests 6-10 → `research-artifacts/usability-tests/batch-2/`
- [ ] **T2.7** Synthesize usability test results → `research-artifacts/analysis/usability-synthesis.md`
  - Metrics: TTFW distribution, friction points, satisfaction ratings, "wow moment" rate
  - Discovery UX preference: Curated vs. browse (% preference, rationale)
  - Trust signals: Creator reputation importance (% who mention, selection behavior)
- [ ] **T2.8** Generate UX friction points report + redesign recommendations (if needed)

### Phase 2 Checkpoint & Decision Gate (End of Week 7)

**Decision Authority**: Product Lead + UX/Design Lead

**Review Criteria**: See `validation-checkpoints.md` → Phase 2 → Phase 3 Gate

- [ ] **Checkpoint 2.1**: Hero Workflow 1 TTFW (≥75% complete in ≤10 min with ≥4/5 satisfaction)
- [ ] **Checkpoint 2.2**: Persona retention ranking (estimated D7/D30 by persona)
- [ ] **Checkpoint 2.3**: Discovery UX preference (curated vs. browse/search)
- [ ] **Checkpoint 2.4**: Creator reputation necessity (build in MVP or defer)

**Decision**:
- **GO**: Launch Phase 3 beta with current UX
- **PIVOT**: Redesign UX friction points (GitHub fork, template customization); re-test with 5 additional users
- **KILL**: TTFW unachievable for non-developers → Pivot to developer-only audience

**Deliverables**:
- [ ] Phase 2 exit report → `research-artifacts/phase-2-exit-report.md`
- [ ] Discovery UX recommendation document (curated vs. browse vs. hybrid)
- [ ] Creator reputation decision (build or defer)

---

## Phase 3: Network Effects & Channel Validation (6-8 weeks)

**Objective**: Validate network effects (R² > 0.4); identify high-quality distribution channels; measure PMF metrics

**Duration**: 6-8 weeks

**Team**: Product Lead (30%), Research Lead (50%), Eng Lead (40%), Design Lead (20%)

**Prerequisites**: Phase 2 PASSED (Hero Workflow 1 validated, UX decided)

### Week 8: Beta Launch Prep

**Tasks**:
- [ ] **T3.1** Finalize MVP marketplace (based on Phase 2 UX decisions)
  - Discovery UX: Curated / browse / hybrid (per Phase 2 decision)
  - Creator reputation: Build / defer (per Phase 2 decision)
- [ ] **T3.2** Seed marketplace with 20-30 high-quality kits (from recruited creators + team-created)
- [ ] **T3.3** Instrument Phase 3 metrics:
  - GitHub API sync (kit metadata: stars, forks, contributors)
  - Vercel Analytics (user behavior: signups, activation, retention)
  - Internal database (forks, submissions, cross-side conversion)
  - UTM tracking (channel attribution)
- [ ] **T3.4** Prepare multi-channel launch assets:
  - Product Hunt listing + screenshots + demo video
  - Twitter thread + demo videos
  - Reddit "I made this" posts (r/ProductManagement, r/marketing, r/SideProject)
  - GitHub repos for trending (standalone kits with links back to marketplace)

### Week 9: Multi-Channel Launch

**Tasks**:
- [ ] **T3.5** Launch on Product Hunt (Week 9, Day 1)
  - Goal: 100+ high-quality signups in first week
  - UTM: `?utm_source=producthunt&utm_medium=launch&utm_campaign=001-marketplace-platform`
- [ ] **T3.6** [P] Twitter campaign (Weeks 9-10)
  - Content: Problem-solution threads, real examples, demo videos
  - Goal: 50+ signups from Twitter
  - UTM: `?utm_source=twitter&utm_medium=social&utm_campaign=001-marketplace-platform`
- [ ] **T3.7** [P] Reddit engagement (Weeks 10-11)
  - Subreddits: r/ProductManagement, r/marketing, r/SideProject
  - Content: "I made this" posts with genuine value
  - Goal: 30+ signups from Reddit
  - UTM: `?utm_source=reddit&utm_medium=community&utm_campaign=001-marketplace-platform`
- [ ] **T3.8** [P] GitHub trending (Weeks 9-12)
  - Seed 10 kits as standalone repos
  - Goal: 1-2 trend on GitHub, drive 50+ signups
  - UTM: `?utm_source=github&utm_medium=organic&utm_campaign=001-marketplace-platform`

### Weeks 10-15: Beta Monitoring & Iteration

**Tasks**:
- [ ] **T3.9** Weekly PMF Review (every Monday, 45 min)
  - Agenda: Metrics review (10 min), learnings (15 min), blockers (10 min), decisions (5 min), next week (5 min)
  - Attendees: Product Lead, Research Lead, Eng Lead, Design Lead
  - Output: Updated dashboard, task priorities, documented decisions
- [ ] **T3.10** Track behavioral metrics (weekly):
  - User signups by channel (UTM)
  - Activation rate by channel (% who fork ≥1 kit)
  - D7/D30 retention by channel
  - Kit count vs. user signups (time series for R² calculation)
  - Cross-side conversion (% users → creators)
  - Creator-to-user ratio
- [ ] **T3.11** Mid-phase checkpoint (Week 11):
  - Channel quality ranking (activation + D7 retention)
  - Decision: Double down on top 2 channels or test new channels
- [ ] **T3.12** Send NPS + Sean Ellis surveys to activated users at Day 30
  - Survey template: See `research-instruments.md` → Survey Template #1
- [ ] **T3.13** Interview 5-10 churned users (optional, if churn >30%)
  - Protocol: "What made you stop using agentii-kit?"

### Phase 3 Checkpoint & Decision Gate (End of Week 15)

**Decision Authority**: Product Lead + Growth Lead

**Review Criteria**: See `validation-checkpoints.md` → Phase 3 → Post-PMF Gate

- [ ] **Checkpoint 3.1**: Network effects validation (R² > 0.4, cross-side conversion ≥10%)
- [ ] **Checkpoint 3.2**: Channel quality ranking (identify 1-2 channels with activation ≥15% AND D7 ≥30%)
- [ ] **Checkpoint 3.3**: Marketplace metrics (D7 ≥30%, D30 ≥20%, MAK ≥50, NPS ≥50, Sean Ellis ≥40%)

**Decision**:
- **SCALE**: PMF achieved → Invest in growth (paid acquisition, content, partnerships); expand categories; add premium features
- **ITERATE**: Weak PMF signals → Run `/pmfkit.optimize` to refine hypotheses; A/B test UX improvements; interview churned users
- **PIVOT**: No PMF → Major pivot required (audience, use case, product model)

**Deliverables**:
- [ ] Phase 3 exit report → `research-artifacts/phase-3-exit-report.md`
- [ ] Channel ranking report (quality vs. volume by channel)
- [ ] Network effects confirmation (R² calculation + cross-side conversion analysis)
- [ ] PMF scorecard (D7/D30 retention, NPS, Sean Ellis test, MAK)

---

## Weekly PMF Review Ritual *(mandatory per constitution)*

**Cadence**: Every Monday, 45 minutes

**Attendees**: Product Lead, Research Lead, Eng Lead, Design Lead

**Agenda**:
1. **Metrics Review** (10 min): Phase-specific numbers (interviews completed, usability tests, signups, retention)
2. **Learnings** (15 min): Quotes, patterns, surprises from research
3. **Blockers** (10 min): Issues slowing progress (recruitment, technical issues, churn)
4. **Decisions** (5 min): Pivot signals, question adjustments, go/no-go at checkpoints
5. **Next Week** (5 min): Task assignments, priorities

**Output**: Updated dashboard + task priorities + documented decisions

---

## Accountability Requirements *(mandatory per constitution)*

### Phase Owners

- **Phase 1**: Research Lead (interviews, synthesis) + Eng Lead (technical validation)
- **Phase 2**: Design Lead (usability tests, UX) + Research Lead (analysis)
- **Phase 3**: Product Lead (metrics, PDCA reviews) + Growth Lead (channels)

### Checkpoint Decision Authority

- **Phase 1 → 2 Gate**: Product Lead + Research Lead
- **Phase 2 → 3 Gate**: Product Lead + UX/Design Lead
- **Phase 3 → Scale Gate**: Product Lead + Growth Lead + CEO (if applicable)

### Weekly PMF Review

- **Attendance Required**: Product Lead, Research Lead, Eng Lead, Design Lead
- **Documentation**: Decision log maintained in `research-artifacts/weekly-reviews/`

---

## Assumptions Documentation *(mandatory per constitution)*

| Assumption | Impact if Invalid | Validation Method | Contingency Plan |
|------------|-------------------|-------------------|-------------------|
| **GitHub remains free for public repos** | High | Monitor GitHub pricing announcements | Contingency plan for GitLab/Codeberg alternatives |
| **AI agents support structured file workflows** | High | Technical validation in Phase 1 (RQ4) | Pivot to single-agent focus if multi-agent fails |
| **Target users (PMs, marketers) are GitHub-literate** | Medium | Usability tests in Phase 2 (RQ2) | Simplify language, add tutorial videos, provide fallback manual editing |
| **Demand for templates is sustainable** | Medium | Behavioral tracking in Phase 3 (repeat usage, retention) | Pivot to different use case or audience if demand drops |
| **Spec-driven methodology adapts to non-coding domains** | High | Interviews + usability tests validate value across marketing, PM, legal, etc. | Focus on developer-adjacent roles if non-devs struggle |

---

## Non-Goals for Research *(mandatory per constitution)*

**Not validating in this research plan**:
- **Payment processing viability**: Monetization deferred to post-PMF; focus on proving free tier value first
- **Private/team kits demand**: MVP is public kits only; private kits validation deferred
- **Kit versioning UI value**: Users manage versions via GitHub; no platform UI validation needed yet
- **Enterprise IT use cases**: We explicitly exclude enterprise procurement teams from personas
- **Non-English markets**: MVP is English-only; internationalization validation deferred

**Not targeting in Phase 1-3**:
- **Advanced search/filters**: Basic browse + keyword search only; advanced filters deferred to post-MVP
- **Kit analytics for creators**: Usage stats deferred to post-PMF; focus on core workflows first
- **API access validation**: Programmatic submission/retrieval not in MVP scope

---

## Next Steps

**Immediate Actions** (Week 1):
1. **Recruit participants**: Screen and schedule 20 interviews + 10 usability tests + 30 creator outreach
2. **Prepare test assets**: Marketplace mockups, sample kits, GitHub repos for testing
3. **Instrument Phase 1 metrics**: Interview synthesis spreadsheet, creator recruitment tracker, compatibility matrix
4. **Schedule Phase 1 Gate Review**: Book 90-minute meeting for end of Week 4

**If Phase 1 Passes**:
- Advance to Phase 2 (usability testing)
- Begin UX mockup creation (curated vs. browse variants)
- Finalize discovery UX based on Phase 2 results

**If Phase 1 Fails**:
- Run `/pmfkit.optimize` to refine hypotheses
- Conduct 5-10 additional interviews with adjusted personas
- Consider major pivot (audience, use case, or product model)

**At Phase Transitions**:
- Run `/pmfkit.optimize` to refine personas, JTBD, and success metrics based on learnings
- Update constitution if thresholds need adjustment (e.g., cross-agent compatibility 70% instead of 80%)
- Document all pivot decisions with rationale in phase exit reports
