# PMF Discovery Task Breakdown: agentii-kit Website

**Branch**: `001-agentii-kit-pmf` | **Date**: 2025-12-04 | **Plan**: [plan.md](./plan.md) | **Spec**: [spec.md](./spec.md)

**Overview**: Research and execution tasks organized by learning objective (research questions) with PDCA cycles. Each research phase has independent validation checkpoints aligned with constitution principles (community-first discovery, customer-evidence-driven validation, measurable learning velocity).

---

## Phase 0: Foundations (Weeks 1-2)

**Objective**: Prepare research infrastructure before Phase 1 interviews

**Duration**: 2 weeks | **Owner**: Product Lead

**Exit Criteria**: 20+ participants recruited; landing page live; research instruments finalized; analytics instrumented

### Research Instrument Preparation

- [ ] T001 Review and finalize Kit Creator interview guide in specs/001-agentii-kit-pmf/research-instruments.md
- [ ] T002 Review and finalize Kit User interview guide in specs/001-agentii-kit-pmf/research-instruments.md
- [ ] T003 Review and finalize User Workflow usability test script in specs/001-agentii-kit-pmf/research-instruments.md
- [ ] T004 Review and finalize Creator Workflow usability test script in specs/001-agentii-kit-pmf/research-instruments.md
- [ ] T005 Create post-session satisfaction survey template in Typeform (8 questions, 1-5 scales + open-ended)

### Participant Recruitment

- [ ] T006 [P] Create screener survey in Google Form or Typeform (6 qualification questions for Kit Creators)
- [ ] T007 [P] Create screener survey in Google Form or Typeform (6 qualification questions for Kit Users)
- [ ] T008 [P] Build Kit Creator recruiting list (15+ candidates from Twitter #PMLife, Reddit r/ProductManagement, LinkedIn PM groups)
- [ ] T009 [P] Build Kit User recruiting list (15+ candidates from Twitter #GrowthMarketing, Reddit r/marketing, r/GrowthHacking)
- [ ] T010 Send outreach DMs to Kit Creator candidates (target: 10 scheduled interviews)
- [ ] T011 Send outreach DMs to Kit User candidates (target: 10 scheduled interviews)
- [ ] T012 Set up Calendly scheduling link for Phase 1 interviews (60-min slots)
- [ ] T013 Schedule first 3 interviews for Week 3 (2 creators, 1 user or vice versa)

### Landing Page & Analytics Setup

- [ ] T014 Draft landing page copy in specs/001-agentii-kit-pmf/landing-page-copy.md (value prop, 3 kit examples, CTA)
- [ ] T015 Design landing page mockup in Figma (homepage, kit card examples, waitlist form)
- [ ] T016 [P] Deploy landing page to kits.agentii.ai via Vercel (Next.js or static HTML)
- [ ] T017 [P] Set up Vercel Analytics on landing page (track visits, UTM sources, bounce rate)
- [ ] T018 [P] Create waitlist form in Typeform (5 fields: email, role, problem, tools, referral source)
- [ ] T019 [P] Embed waitlist Typeform on landing page
- [ ] T020 Set up GitHub API access for future kit tracking (create personal access token, test forks/stars API)
- [ ] T021 Create Notion synthesis dashboard (tables: interviews, personas, JTBD, quotes, willingness-to-pay)

### Landing Page Soft Launch

- [ ] T022 Soft-launch landing page to personal network (Twitter post, LinkedIn post, 2-3 Reddit comments)
- [ ] T023 Monitor landing page for 48 hours (track visits, waitlist signups, bounce rate)
- [ ] T024 Adjust landing page copy based on initial feedback (if bounce > 80% or < 2% conversion)

### Phase 0 Checkpoint

- [ ] T025 Phase 0 exit review (Monday, End of Week 2)
  - Check: 20+ participants recruited? Landing page live? Analytics working? Research instruments finalized?
  - GO: All criteria met → Advance to Phase 1
  - DELAY: < 15 participants → Extend Phase 0 by 1 week; leverage snowball sampling
  - Decision documented in specs/001-agentii-kit-pmf/phase-0-decision.md

---

## Phase 1: Persona & Problem Validation (Weeks 3-6)

**Objective**: Confirm personas and JTBD are real, urgent, and worth solving for BOTH creators and users (Principle I: Two-Sided Marketplace Validation)

**Duration**: 4 weeks | **Owner**: Product Lead

**Exit Criteria**: 18-20 interviews completed; 70%+ report 2+ hrs/week pain; 60%+ willingness-to-try; 40%+ willing to pay $5-20/mo

### Interview Execution (Week 3-4)

- [ ] T026 [P] [RQ1] Conduct Kit Creator interview #1 (60 min, record with consent, synthesize in Notion)
- [ ] T027 [P] [RQ1] Conduct Kit Creator interview #2
- [ ] T028 [P] [RQ1] Conduct Kit User interview #1
- [ ] T029 [P] [RQ1] Conduct Kit User interview #2
- [ ] T030 [P] [RQ1] Conduct Kit Creator interview #3
- [ ] T031 [P] [RQ1] Conduct Kit User interview #3
- [ ] T032 [P] [RQ1] Conduct Kit Creator interview #4
- [ ] T033 [P] [RQ1] Conduct Kit User interview #4
- [ ] T034 [RQ1] Synthesize first 8 interviews in Notion (tag: persona, JTBD mentions, pain frequency, willingness-to-pay)

### Week 4 Mid-Phase Checkpoint

- [ ] T035 Week 4 mid-phase decision (Monday, End of Week 4)
  - Check: Are patterns emerging? 70%+ pain frequency? JTBD consistent? Willingness-to-pay signals?
  - GO: Strong signals → Continue with remaining 10 interviews
  - PIVOT: Different JTBD emerges → Adjust interview guide; recruit 5 more for new persona
  - NO-GO: < 50% pain frequency → Pause Phase 1; escalate to stakeholders
  - Decision documented in specs/001-agentii-kit-pmf/phase-1-mid-decision.md

### Interview Execution (Week 5-6)

- [ ] T036 [P] [RQ1] Conduct Kit Creator interview #5
- [ ] T037 [P] [RQ1] Conduct Kit Creator interview #6
- [ ] T038 [P] [RQ1] Conduct Kit User interview #5
- [ ] T039 [P] [RQ1] Conduct Kit User interview #6
- [ ] T040 [P] [RQ1] Conduct Kit Creator interview #7
- [ ] T041 [P] [RQ1] Conduct Kit User interview #7
- [ ] T042 [P] [RQ1] Conduct Kit Creator interview #8
- [ ] T043 [P] [RQ1] Conduct Kit User interview #8
- [ ] T044 [P] [RQ1] Conduct Kit Creator interview #9
- [ ] T045 [P] [RQ1] Conduct Kit User interview #9
- [ ] T046 [P] [RQ1] Conduct Kit Creator interview #10
- [ ] T047 [P] [RQ1] Conduct Kit User interview #10

### Synthesis & Analysis

- [ ] T048 [RQ1] Finalize persona profiles in specs/001-agentii-kit-pmf/personas.md (2-3 primary personas with verbatim quotes)
- [ ] T049 [RQ1] Create JTBD evidence summary in specs/001-agentii-kit-pmf/jtbd-validation.md (mention rates, frequency, pain intensity)
- [ ] T050 [RQ2] Document willingness-to-pay findings in specs/001-agentii-kit-pmf/willingness-to-pay.md (% willing, price thresholds, premium features)
- [ ] T051 [RQ2] Analyze incumbent pain points in specs/001-agentii-kit-pmf/competitive-gaps.md (PromptBase, Notion, ChatGPT gaps with quotes)
- [ ] T052 [RQ1] Calculate JTBD mention rates (JTBD #1: X%, JTBD #2: X%, JTBD #3: X%)
- [ ] T053 [RQ1] Calculate pain frequency (X% report 2+ hrs/week)
- [ ] T054 [RQ2] Calculate willingness-to-pay (X% willing to pay $5-20/mo)

### Phase 1 Exit Criteria Review

- [ ] T055 Phase 1 exit review (Monday, End of Week 6)
  - Check: 70%+ report 2+ hrs/week pain? 60%+ willingness-to-try? 40%+ willing to pay? 100+ landing page signups?
  - GO: All criteria met → Advance to Phase 2
  - PIVOT: Adjacent persona stronger (Eng Managers 90% vs PMs 60%) → Shift focus to technical users first
  - PIVOT: Different JTBD emerges → Refocus spec.md
  - NO-GO: Pain signals weak (< 50% report 2+ hrs/week) → Kill hypothesis; explore alternatives
  - Decision documented in specs/001-agentii-kit-pmf/phase-1-decision.md

### Phase 2 Prep (if GO)

- [ ] T056 Recruit 10 PM/marketer participants for user workflow usability tests from Phase 1 pool
- [ ] T057 Recruit 8 PM/marketer creators for creator workflow usability tests from Phase 1 pool
- [ ] T058 Schedule usability tests for Phase 2 (10 user workflow, 8 creator workflow, spread across Weeks 7-10)

---

## Phase 2: Hero Workflow Validation (Weeks 7-10)

**Objective**: Ensure both hero workflows deliver value; validate TTFW targets; mitigate GitHub barrier (Principle IV: GitHub-Native Distribution, Principle V: Progressive Disclosure)

**Duration**: 4 weeks | **Owner**: Product + Design Leads

**Exit Criteria**: 75%+ user workflow completion; 70%+ meet TTFW < 10 min; satisfaction >= 4.0; 80%+ creator workflow completion; 70%+ rate curation 4+ stars

### Usability Test Preparation

- [ ] T059 Create user workflow test scenario doc in specs/001-agentii-kit-pmf/user-workflow-scenario.md ("Find marketing campaign brief kit")
- [ ] T060 Create creator workflow test scenario doc in specs/001-agentii-kit-pmf/creator-workflow-scenario.md ("Submit PM PRD template")
- [ ] T061 [P] Create mockup of landing page + kit gallery in Figma (for user workflow tests)
- [ ] T062 [P] Create mockup of kit detail page + fork flow in Figma (for user workflow tests)
- [ ] T063 [P] Create mockup of submission form + curation feedback in Figma (for creator workflow tests)
- [ ] T064 Set up Zoom for usability tests (screen share, recording, think-aloud protocol instructions)

### User Workflow Usability Tests (Week 7-8)

- [ ] T065 [P] [RQ3] Run user workflow test #1 (PM persona, measure TTFW, tag friction points in Notion)
- [ ] T066 [P] [RQ3] Run user workflow test #2 (Marketer persona)
- [ ] T067 [P] [RQ3] Run user workflow test #3 (PM persona)
- [ ] T068 [RQ3] Analyze first 3 user tests (identify top 3 friction points: GitHub barrier, unclear instructions, missing features)
- [ ] T069 [RQ3] Make quick non-technical fixes (copy changes, reorder steps, add tooltips to mockups)

- [ ] T070 [P] [RQ3] Run user workflow test #4 (with fixes applied)
- [ ] T071 [P] [RQ3] Run user workflow test #5
- [ ] T072 [P] [RQ3] Run user workflow test #6
- [ ] T073 [RQ3] Calculate TTFW distribution for first 6 tests (min, median, max, % under 10 min)
- [ ] T074 [RQ3] Calculate completion rate (X/6 successfully completed)

### Creator Workflow Usability Tests (Week 7-8)

- [ ] T075 [P] [RQ4] Run creator workflow test #1 (measure submission time, test curation feedback satisfaction)
- [ ] T076 [P] [RQ4] Run creator workflow test #2
- [ ] T077 [P] [RQ4] Run creator workflow test #3
- [ ] T078 [P] [RQ4] Run creator workflow test #4
- [ ] T079 [RQ4] Analyze first 4 creator tests (curation satisfaction, abandonment intent, metadata quality)

### Week 8 Mid-Phase Checkpoint

- [ ] T080 Week 8 mid-phase decision (Monday, End of Week 8)
  - Check: TTFW < 10 min for 70%+? Satisfaction >= 4.0? Submission < 5 min for 80%+? Curation 4+ stars?
  - GO: Strong signals → Continue with remaining tests
  - PIVOT: GitHub barrier insurmountable (< 50% completion) → Test "Kit Runner" web UI alternative
  - NO-GO: Satisfaction < 3.5, TTFW 30%+ over target → Pause Phase 2; redesign workflow
  - Decision documented in specs/001-agentii-kit-pmf/phase-2-mid-decision.md

### User Workflow Usability Tests (Week 9-10)

- [ ] T081 [P] [RQ3] Run user workflow test #7
- [ ] T082 [P] [RQ3] Run user workflow test #8
- [ ] T083 [P] [RQ3] Run user workflow test #9
- [ ] T084 [P] [RQ3] Run user workflow test #10
- [ ] T085 [RQ3] Calculate final TTFW distribution (all 10 tests)
- [ ] T086 [RQ3] Calculate final completion rate and satisfaction avg

### Creator Workflow Usability Tests (Week 9-10)

- [ ] T087 [P] [RQ4] Run creator workflow test #5
- [ ] T088 [P] [RQ4] Run creator workflow test #6
- [ ] T089 [P] [RQ4] Run creator workflow test #7
- [ ] T090 [P] [RQ4] Run creator workflow test #8
- [ ] T091 [RQ4] Calculate final submission time distribution (all 8 tests)
- [ ] T092 [RQ4] Calculate final curation satisfaction and abandonment rate

### Synthesis & Reporting

- [ ] T093 [RQ3] Create user workflow test summary in specs/001-agentii-kit-pmf/user-workflow-summary.md (TTFW, completion, friction points, quotes)
- [ ] T094 [RQ4] Create creator workflow test summary in specs/001-agentii-kit-pmf/creator-workflow-summary.md (submission time, curation satisfaction, quotes)
- [ ] T095 Prioritize friction points for Phase 3 (top 3 with fix roadmap)

### Phase 2 Exit Criteria Review

- [ ] T096 Phase 2 exit review (Monday, End of Week 10)
  - Check: 75%+ user completion? 70%+ TTFW < 10 min? >= 4.0 satisfaction? 80%+ creator completion? 70%+ curation 4+ stars?
  - GO: All criteria met → Advance to Phase 3
  - PIVOT: GitHub barrier (< 60% completion) → Test Kit Runner web UI
  - PIVOT: Persona mismatch (Eng Managers 90%, Marketers 50%) → Target technical users first
  - NO-GO: < 50% completion after fixes → Workflow too complex; redesign required
  - Decision documented in specs/001-agentii-kit-pmf/phase-2-decision.md

### Phase 3 Prep (if GO)

- [ ] T097 Recruit 5-10 founding creators from Phase 1/2 to create seed kits
- [ ] T098 Recruit 50+ beta testers from waitlist + Phase 1/2 participants

---

## Phase 3: MVP Beta & Channel Validation (Weeks 11-16)

**Objective**: Launch curated MVP; validate network effects; identify highest-quality acquisition channel (Principle VI: Measurable Learning Velocity)

**Duration**: 6 weeks | **Owner**: Growth + Product Leads

**Exit Criteria**: Activation 15%+; D7 retention 30%+; clear winner channel (2x better); R² > 0.6; 10%+ cross-side conversion; 100+ activated users; 20+ kits live

### Seed Kit Creation (Week 11-12)

- [ ] T099 [P] Create PM-Kit #1 (PRD template) in seed-kits/pm-kit-1/ directory
- [ ] T100 [P] Create PM-Kit #2 (Roadmap template) in seed-kits/pm-kit-2/ directory
- [ ] T101 [P] Create Marketing-Kit #1 (Campaign brief template) in seed-kits/marketing-kit-1/ directory
- [ ] T102 [P] Create Marketing-Kit #2 (Content strategy template) in seed-kits/marketing-kit-2/ directory
- [ ] T103 [P] Create Legal-Kit #1 (Contract review template) in seed-kits/legal-kit-1/ directory
- [ ] T104 [P] Create Edu-Kit #1 (Lesson plan template) in seed-kits/edu-kit-1/ directory
- [ ] T105 Recruit 5-10 founding creators to submit 4-9 additional kits (target: 10-15 total seed kits)
- [ ] T106 Review founding creator kits for quality (completeness, clarity, tested, differentiated)
- [ ] T107 Approve 10-15 seed kits for launch

### MVP Deploy (Week 12)

- [ ] T108 Deploy MVP to kits.agentii.ai (functional fork flow, submission flow, kit gallery)
- [ ] T109 [P] Instrument Vercel Analytics (track visits, signups, UTM sources)
- [ ] T110 [P] Instrument GitHub API tracking (forks, stars, kit submissions)
- [ ] T111 [P] Create UTM tracking links for each channel (PH, Twitter, Reddit, Content)
- [ ] T112 Set up Notion metrics dashboard (visits, signups, activations, retention by channel)
- [ ] T113 Test MVP end-to-end (browse → fork → submit kit → manual curation)

### Product Hunt Launch Prep (Week 12)

- [ ] T114 [RQ6] Create Product Hunt assets (video demo, 3-5 screenshots, tagline, description)
- [ ] T115 [RQ6] Write Product Hunt launch post copy in specs/001-agentii-kit-pmf/ph-launch-copy.md
- [ ] T116 [RQ6] Recruit Product Hunt hunter (if needed)
- [ ] T117 [RQ6] Schedule PH launch for Week 13 Day 1 (Tuesday 12:01am PST)

### Twitter Launch Prep (Week 12)

- [ ] T118 [P] [RQ6] Draft Twitter thread (8-10 tweets) in specs/001-agentii-kit-pmf/twitter-thread.md
- [ ] T119 [P] [RQ6] Create demo screenshots for Twitter thread
- [ ] T120 [P] [RQ6] Schedule Twitter thread for Week 13 Day 3 (Thursday 10am EST)

### Reddit Launch Prep (Week 12)

- [ ] T121 [P] [RQ6] Draft Reddit posts for r/ProductManagement and r/marketing in specs/001-agentii-kit-pmf/reddit-posts.md
- [ ] T122 [P] [RQ6] Schedule Reddit posts for Week 13 Day 5 (Saturday)

### Content Marketing Prep (Week 12)

- [ ] T123 [P] [RQ6] Write SEO-optimized guide #1 ("How to write a PRD in 10 minutes with AI") in blog/guide-1.md
- [ ] T124 [P] [RQ6] Write SEO-optimized guide #2 ("How to structure marketing campaigns with templates") in blog/guide-2.md

### Channel Execution (Week 13)

- [ ] T125 [RQ6] Execute Product Hunt launch (Week 13 Day 1)
- [ ] T126 [RQ6] Monitor PH launch (respond to comments, thank upvoters, track metrics)
- [ ] T127 [RQ6] Execute Twitter thread launch (Week 13 Day 3)
- [ ] T128 [RQ6] Execute Reddit posts (Week 13 Day 5, r/ProductManagement and r/marketing)
- [ ] T129 [RQ6] Monitor daily metrics (visits, signups, activations by channel)

### Content Marketing Execution (Week 14-16)

- [ ] T130 [P] [RQ6] Publish blog guide #1 (Week 14)
- [ ] T131 [P] [RQ6] Publish blog guide #2 (Week 14)
- [ ] T132 [RQ6] Promote guides on Twitter and Reddit (cross-post links)

### Network Effects Measurement (Week 13-16)

- [ ] T133 [RQ5] Track kit submission events (timestamp, creator ID, social shares)
- [ ] T134 [RQ5] Track user signup events (timestamp, UTM source, referred by kit?)
- [ ] T135 [RQ5] Track cross-side conversion (user ID → creator ID, first kit submission date)
- [ ] T136 [RQ5] Calculate kit → user correlation (plot scatter, measure R²)
- [ ] T137 [RQ5] Calculate cross-side conversion rate (% users → creators within 30 days)

### Week 15 Analysis Week

- [ ] T138 [RQ6] Create cohort analysis by channel in specs/001-agentii-kit-pmf/channel-cohorts.md (activation, D7 retention)
- [ ] T139 [RQ6] Calculate combined score for each channel (activation × D7 retention)
- [ ] T140 [RQ6] Identify winner channel (2x better than second place)
- [ ] T141 [RQ5] Plot network effects scatter (kit count → user signups, show R²)
- [ ] T142 [RQ5] Document network effects findings in specs/001-agentii-kit-pmf/network-effects-analysis.md

### Week 16 Final Decisions

- [ ] T143 Double down on winner channel (allocate remaining budget/effort)
- [ ] T144 Kill low-performing channels (< 10% activation or < 20% D7 retention)
- [ ] T145 Document acquisition playbook for winner channel in specs/001-agentii-kit-pmf/acquisition-playbook.md (audience, messaging, timing, format, budget)

### Phase 3 Exit Criteria Review

- [ ] T146 Phase 3 exit review (Monday, End of Week 16)
  - Check: 15%+ activation? 30%+ D7 retention? Clear winner? R² > 0.6? 10%+ cross-side conversion? 100+ activated users? 20+ kits live?
  - GO/SCALE: All criteria met → Proceed to broader launch (expand channels, recruit creators, build automation)
  - PIVOT: No clear winner (all < 15% activation) → Revisit value prop; test alternative headlines
  - PIVOT: Network effects weak (R² < 0.4) → Explore alternative models (SaaS subscription vs marketplace)
  - NO-GO: All channels < 10% activation → Kill hypothesis; revisit JTBD from Phase 1
  - Decision documented in specs/001-agentii-kit-pmf/phase-3-decision.md

---

## Cross-Phase: Continuous Rituals

### Weekly PMF Reviews

- [ ] T147 Run Weekly PMF Review #1 (Monday Week 3, Phase 1 start)
- [ ] T148 Run Weekly PMF Review #2 (Monday Week 4)
- [ ] T149 Run Weekly PMF Review #3 (Monday Week 5)
- [ ] T150 Run Weekly PMF Review #4 (Monday Week 6)
- [ ] T151 Run Weekly PMF Review #5 (Monday Week 7, Phase 2 start)
- [ ] T152 Run Weekly PMF Review #6 (Monday Week 8)
- [ ] T153 Run Weekly PMF Review #7 (Monday Week 9)
- [ ] T154 Run Weekly PMF Review #8 (Monday Week 10)
- [ ] T155 Run Weekly PMF Review #9 (Monday Week 11, Phase 3 start)
- [ ] T156 Run Weekly PMF Review #10 (Monday Week 12)
- [ ] T157 Run Weekly PMF Review #11 (Monday Week 13)
- [ ] T158 Run Weekly PMF Review #12 (Monday Week 14)
- [ ] T159 Run Weekly PMF Review #13 (Monday Week 15)
- [ ] T160 Run Weekly PMF Review #14 (Monday Week 16)

**Agenda for each review** (45 min):
1. Metrics review (10 min): Phase-specific numbers (interviews, usability tests, or channel performance)
2. Learnings (15 min): Quotes, patterns, surprises, contradictory evidence
3. Blockers (10 min): Participant no-shows, tool issues, unclear findings
4. Decisions (5 min): Pivot persona? Adjust questions? Extend phase?
5. Next week focus (5 min): Task assignments, priorities

### Documentation

- [ ] T161 Maintain running research synthesis doc in specs/001-agentii-kit-pmf/synthesis.md (update weekly with quotes, JTBD evidence, hypotheses)
- [ ] T162 Create Phase 1 summary after Week 6 in specs/001-agentii-kit-pmf/phase-1-summary.md
- [ ] T163 Create Phase 2 summary after Week 10 in specs/001-agentii-kit-pmf/phase-2-summary.md
- [ ] T164 Create Phase 3 summary after Week 16 in specs/001-agentii-kit-pmf/phase-3-summary.md

---

## Dependencies & Critical Path

### Phase Dependencies

- **Phase 0** MUST complete before Phase 1 (need participants recruited + instruments ready)
- **Phase 1** MUST complete before Phase 2 (need validated personas + JTBD before testing workflows)
- **Phase 2** MUST complete before Phase 3 (need successful hero workflow before channel testing)

### Critical Path Tasks

**Phase 0 Critical**:
- T010, T011 (Participant recruitment) - 2-week lead time drives timeline
- T016 (Landing page deploy) - Blocks T022 (soft launch)

**Phase 1 Critical**:
- T026-T047 (All 20 interviews) - Must complete before T048-T055 (synthesis)
- T035 (Mid-phase decision) - Could trigger pivot/no-go

**Phase 2 Critical**:
- T061-T063 (Mockups) - Block all usability tests
- T065-T084 (User workflow tests) - Must complete before T085-T086 (final analysis)
- T080 (Mid-phase decision) - Could trigger GitHub barrier pivot

**Phase 3 Critical**:
- T099-T107 (Seed kits) - Block T108 (MVP deploy)
- T108 (MVP deploy) - Blocks T125 (PH launch)
- T125 (PH launch) - First channel test, drives Week 13 metrics

**Total Duration**: 16 weeks (2+4+4+6) for full PMF discovery cycle

---

## Parallel Execution Opportunities

### Phase 0 Parallelization

**Group 1** (T006-T009): All screener surveys and recruiting lists can run in parallel (4 tasks)
**Group 2** (T016-T020): Landing page deploy, Vercel Analytics, Typeform, GitHub API, Notion dashboard (5 tasks)

### Phase 1 Parallelization

**Interview Execution**: T026-T033 (first 8 interviews) can run in parallel if multiple interviewers available. Same for T036-T047 (remaining 10 interviews).

**Best Practice**: Schedule 4-5 interviews per week spread across days to allow synthesis time.

### Phase 2 Parallelization

**Mockup Creation**: T061-T063 can run in parallel (3 tasks)
**Usability Tests**: T065-T067 (first 3 user tests) can run in parallel if multiple facilitators. Same for T070-T072, T075-T079, T081-T084, T087-T090.

**Best Practice**: Run 2-3 tests per week to allow friction point analysis between batches.

### Phase 3 Parallelization

**Seed Kit Creation**: T099-T104 can run in parallel (6 tasks)
**Analytics Setup**: T109-T111 can run in parallel (3 tasks)
**Launch Prep**: T118-T119 (Twitter), T121-T122 (Reddit), T123-T124 (Content) can all run in parallel (6 tasks)
**Content Publishing**: T130-T131 can run in parallel (2 tasks)

---

## Independent Test Criteria by Research Question

### RQ1: Persona & JTBD Validation

**Test Criteria**:
- 70%+ of interviewed personas report spending 2+ hours/week on workflow setup
- 60%+ mention actively searching for "templates," "automation," or "AI workflows"
- JTBD #1 mentioned by 80%+, JTBD #2 by 50%+, JTBD #3 by 70%+

**Verification Method**: Count persona responses in Notion synthesis dashboard; calculate mention rates

**Independence**: Phase 1 can be validated without Phase 2 or 3 data

### RQ2: Willingness-to-Pay Validation

**Test Criteria**:
- 80%+ mention specific incumbent pain points (PromptBase, Notion, ChatGPT gaps)
- 50%+ indicate they'd pay $5-20/mo for premium features
- Landing page waitlist: 100+ signups (5%+ conversion from organic/paid traffic)

**Verification Method**: Quote analysis + landing page analytics

**Independence**: Can be validated within Phase 1 + Phase 0 landing page data

### RQ3: User Workflow Validation

**Test Criteria**:
- 75%+ of non-technical users successfully complete workflow (fork kit + understand Quick Start)
- 70%+ complete workflow in < 10 min
- Avg satisfaction >= 4.0/5.0

**Verification Method**: TTFW timer + completion tracking + post-session survey

**Independence**: Phase 2 user workflow tests are independent of creator workflow tests

### RQ4: Creator Workflow Validation

**Test Criteria**:
- 80%+ successfully submit kit in < 5 min
- 70%+ rate curation feedback 4+ stars (even if rejected)
- < 10% abandonment rate after rejection

**Verification Method**: Submission time timer + curation satisfaction survey

**Independence**: Phase 2 creator workflow tests are independent of user workflow tests

### RQ5: Network Effects Validation

**Test Criteria**:
- Each kit submission drives 5+ new users within 7 days (on average)
- Cross-side conversion 10%+ (10+ users out of 100 become creators within 30 days)
- R² > 0.6 for kit count → user signup correlation

**Verification Method**: Behavioral analytics (kit events, user signups, cross-side conversion tracking)

**Independence**: Phase 3 network effects can be measured independently once MVP launched

### RQ6: Channel Validation

**Test Criteria**:
- At least 1 channel has activation 15%+ AND D7 retention 30%+
- Clear winner channel (combined score 2x+ better than second place)
- Winner channel is repeatable (consistent over 2+ weeks)

**Verification Method**: Cohort analysis by UTM source; activation × retention scoring

**Independence**: Each channel can be tested independently with separate UTM tracking

---

## Implementation Strategy

### MVP Scope (Phase 3 Minimum)

**What's Included**:
- Landing page with kit gallery (10-15 seed kits)
- GitHub fork flow (OAuth + one-click fork)
- Kit submission flow (GitHub OAuth + metadata form)
- Manual curation (founder reviews submissions in 24-48 hours)
- Waitlist form (Typeform)
- Analytics (Vercel Analytics + GitHub API + UTM tracking)

**What's Excluded** (post-PMF):
- Automated quality checks
- Advanced search/filters
- User accounts/profiles
- Creator dashboards
- Team accounts
- Private kits
- Premium features
- Payment processing

### Incremental Delivery Approach

**Phase 0 Deliverable**: Landing page + waitlist (baseline demand signal)
**Phase 1 Deliverable**: Validated personas + JTBD with evidence (interview synthesis)
**Phase 2 Deliverable**: Validated hero workflows with TTFW data (usability test summaries)
**Phase 3 Deliverable**: MVP launched; winner channel identified; network effects measured (acquisition playbook)

### Success Metrics Summary

By end of all phases, we will have:

✅ **Persona Clarity**: 70%+ of target personas report 2+ hrs/week pain; willingness-to-try evident
✅ **JTBD Validation**: Top 3 JTBD confirmed through interviews; mention rates documented
✅ **Willingness-to-Pay**: 40%+ willing to pay $5-20/mo; premium features prioritized
✅ **Hero Workflows Proven**: 75%+ user completion; 80%+ creator completion; TTFW targets met
✅ **Network Effects**: R² > 0.6; 10%+ cross-side conversion; marketplace dynamics validated
✅ **Go-to-Market Path**: Clear winner channel (2x better); activation 15%+; D7 retention 30%+
✅ **PMF Decision**: GO/SCALE, PIVOT, or NO-GO with confidence and data

---

## Format Validation

**Total Tasks**: 164 tasks
**Task Distribution**:
- Phase 0 (Foundations): 25 tasks
- Phase 1 (Persona & Problem): 31 tasks
- Phase 2 (Hero Workflows): 39 tasks
- Phase 3 (MVP Beta & Channels): 48 tasks
- Cross-Phase (Rituals): 21 tasks

**Parallel Opportunities**: 55 tasks marked [P] across all phases

**Research Questions Mapped**:
- RQ1 (Persona & JTBD): 28 tasks
- RQ2 (Willingness-to-Pay): 6 tasks
- RQ3 (User Workflow): 22 tasks
- RQ4 (Creator Workflow): 18 tasks
- RQ5 (Network Effects): 5 tasks
- RQ6 (Channel Validation): 25 tasks

**All tasks follow checklist format**: ✅ Checkbox + TaskID + [P] (if parallel) + [RQ#] (research question label) + Description with file path

**Independent Test Criteria**: Defined for all 6 research questions with verification methods

**Suggested MVP Scope**: Phase 3 minimum (landing page, fork flow, submission, manual curation, analytics)
