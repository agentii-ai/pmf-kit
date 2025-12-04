# Validation Checkpoints: agentii-kit PMF Discovery

**Feature**: 001-agentii-kit-pmf
**Created**: 2025-12-04
**Status**: Active Research

---

## Overview

This document defines PDCA (Plan-Do-Check-Act) cycle gates for each research phase with explicit go/kill/pivot criteria. All checkpoints include weekly review agendas and phase-end decision frameworks per constitution Principle III (Iterative Validation).

---

## Phase 0: Foundations (Weeks 1-2)

**Goal**: Prepare research infrastructure before Phase 1 interviews

### Week 1 Checkpoint (Monday, End of Week 1)

**Check**:
- [ ] Research instruments finalized (interview guides, usability scripts, survey templates reviewed)
- [ ] Participant recruitment started (10+ candidates contacted via Twitter/Reddit/LinkedIn)
- [ ] Landing page copy drafted (value prop, CTA, kit examples)
- [ ] Analytics tools identified (Vercel Analytics, Typeform, GitHub API, Notion)

**Act**:
- If instruments need revision → Incorporate feedback from reviewer
- If recruitment slow → Increase incentive ($50 → $75) or expand sourcing channels
- If landing page copy unclear → A/B test 2 headlines

### Week 2 Checkpoint (Monday, End of Week 2)

**Check**:
- [ ] 20+ qualified participants recruited (10 creators, 10 users)
- [ ] Landing page live at kits.agentii.ai with analytics instrumented
- [ ] Notion synthesis dashboard set up (persona tags, quote fields, JTBD categories)
- [ ] First 3 interviews scheduled for Week 3

**Act**:
- If < 20 participants → Extend Phase 0 by 1 week; leverage snowball sampling from first interviews
- If landing page not live → Delay Phase 1 start; prioritize deployment

**Phase 0 Exit Criteria** (Go/No-Go to Phase 1):
- [ ] **GO**: 20+ participants recruited; landing page live; research instruments finalized
- [ ] **DELAY**: < 15 participants recruited → Extend Phase 0 by 1 week
- [ ] **NO-GO**: Unable to recruit participants after 4 weeks → Revisit persona targeting (pivot to Eng Managers?)

---

## Phase 1: Persona & Problem Validation (Weeks 3-6)

**Goal**: Confirm personas and JTBD are real, urgent, and worth solving

### Weekly PDCA Checkpoints

#### Week 3 Checkpoint (Monday, End of Week 3)

**Check** (after 4-5 interviews completed):
- [ ] Are personas reporting 2+ hours/week pain? (count: [X]/5)
- [ ] Are JTBD themes emerging? (Discover: [X] mentions, Share: [X] mentions, Validate: [X] mentions)
- [ ] Are willingness-to-pay signals present? (count: [X]/5)
- [ ] Are quotes capturing verbatim pain descriptions?

**Act**:
- If pain frequency < 60% → Adjust interview questions to probe deeper ("How would 2 hours/week time savings impact your work?")
- If JTBD mismatch → Pivot questions to explore alternative jobs ("What would you pay for instead?")
- If recruitment lag → Reach out to Phase 1 participants for referrals (snowball sampling)

#### Week 4 Checkpoint (Monday, End of Week 4)

**Check** (after 8-10 interviews completed - **MID-PHASE DECISION POINT**):
- [ ] Are patterns emerging? (70%+ consistency in pain frequency, JTBD mentions)
- [ ] Do personas feel distinct? (Kit Creators vs Kit Users showing different motivations)
- [ ] Are competitive alternatives mentioned? (PromptBase, Notion, ChatGPT - count by tool)
- [ ] Are willingness-to-pay thresholds clear? ($5/mo vs $20/mo preferences)

**Act - MID-PHASE DECISION**:
- **If GO signals strong** (70%+ pain frequency, consistent JTBD) → Continue Phase 1 with remaining 10 interviews
- **If PIVOT signals** (different JTBD emerges, or adjacent persona stronger) → Adjust interview guide; recruit 5 more interviews for new persona
- **If NO-GO signals** (< 50% pain frequency, no willingness-to-try) → Pause Phase 1; escalate to Phase-End Review early

#### Week 5 Checkpoint (Monday, End of Week 5)

**Check** (after 13-15 interviews completed):
- [ ] JTBD priority validated? (JTBD #1 mentioned by 80%+, JTBD #2 by 50%+, JTBD #3 by 70%+)
- [ ] Willingness-to-pay confirmed? (40%+ willing to pay $5-20/mo)
- [ ] Incumbent pain points clear? (80%+ mention specific gaps in PromptBase/Notion/ChatGPT)
- [ ] Participant pool recruited for Phase 2? (8-10 usability test participants)

**Act**:
- If JTBD priority unclear → Conduct 2-3 additional interviews with edge cases
- If willingness-to-pay low → Explore alternative monetization (creator fees, enterprise tiers)
- If Phase 2 recruitment weak → Offer Phase 1 interviewees early access incentive

#### Week 6 Checkpoint (Monday, End of Week 6)

**Check** (after 18-20 interviews completed):
- [ ] Phase 1 exit criteria met? (see below)
- [ ] Persona profiles finalized? (2-3 primary personas with quotes)
- [ ] JTBD evidence documented? (mention rates, frequency, pain intensity)
- [ ] Willingness-to-pay summary complete? (% willing to pay, price thresholds, premium features)

**Act**:
- If exit criteria met → Advance to Phase 2
- If exit criteria partially met → Identify gaps; conduct 3-5 additional targeted interviews
- If exit criteria not met → Escalate to Phase-End Review for pivot decision

---

### Phase 1 Exit Criteria (Go/Pivot/No-Go Decision)

**GO Criteria** (all must pass):
- [ ] **Persona validation**: 70%+ of creators report 2+ hours/week pain; 70%+ of users report same
- [ ] **JTBD clarity**: JTBD #1 mentioned by 80%+; JTBD #2 by 50%+; JTBD #3 by 70%+
- [ ] **Willingness-to-try**: 60%+ express enthusiasm ("I'd try this immediately" or equivalent)
- [ ] **Willingness-to-pay**: 40%+ indicate they'd pay $5-20/mo for premium features
- [ ] **Incumbent pain**: 80%+ mention specific gaps in free alternatives
- [ ] **Landing page demand**: 100+ waitlist signups from organic/paid traffic (5%+ conversion)

**PIVOT Criteria** (adjust focus):
- [ ] **Adjacent persona stronger**: Eng Managers show 90%+ pain vs 60% for PMs → Shift focus to technical users first
- [ ] **Different JTBD**: "Collaborate on kits" emerges as higher priority than "Discover kits" → Refocus spec
- [ ] **Domain pivot**: Legal Ops or Educators report higher pain/frequency than PM/Marketing → Expand target segments

**NO-GO Criteria** (kill hypothesis):
- [ ] **Pain signals weak**: < 50% report 2+ hours/week pain
- [ ] **No willingness-to-try**: < 40% express enthusiasm
- [ ] **No differentiation**: < 50% perceive value beyond free alternatives
- [ ] **Landing page failure**: < 2% conversion (< 40 signups from 2000 visits)

**Decision Owner**: Product Lead
**Decision Date**: End of Week 6 (Monday)
**Decision Format**: Phase-End Review meeting (90 min) with stakeholders

---

## Phase 2: Hero Workflow Validation (Weeks 7-10)

**Goal**: Ensure both hero workflows deliver value; validate TTFW targets; mitigate GitHub barrier

### Weekly PDCA Checkpoints

#### Week 7 Checkpoint (Monday, End of Week 7)

**Check** (after 2-3 user workflow tests + 2 creator workflow tests):
- [ ] User workflow: TTFW distribution? (min: [X] min, median: [X] min, max: [X] min)
- [ ] User workflow: Completion rate? ([X]/3 completed successfully)
- [ ] User workflow: GitHub barrier friction? ([X]/3 got stuck at GitHub OAuth)
- [ ] Creator workflow: Submission time? (median: [X] min)
- [ ] Creator workflow: Metadata quality? ([X]/2 complete, [X]/2 missing fields)

**Act**:
- If TTFW > 15 min for 60%+ → Identify bottleneck (GitHub OAuth? Unclear instructions?); test Quick Start video mitigation
- If GitHub barrier high (> 50% stuck) → Prepare "Kit Runner" web UI prototype for Week 9 testing
- If metadata incomplete → Simplify form (fewer required fields, inline examples)

#### Week 8 Checkpoint (Monday, End of Week 8) - **MID-PHASE DECISION POINT**

**Check** (after 5 user + 4 creator tests - **HALFWAY POINT**):
- [ ] User workflow: TTFW < 10 min achieved by X%? (target: 70%+)
- [ ] User workflow: Satisfaction >= 4.0 avg? (current: [X.X]/5.0)
- [ ] Creator workflow: Submission < 5 min achieved by X%? (target: 80%+)
- [ ] Creator workflow: Curation feedback satisfaction? (current: [X.X]/5.0)
- [ ] Friction points clear? (top 3 friction points identified + counts)

**Act - MID-PHASE DECISION**:
- **If GO signals strong** (70%+ meeting TTFW, satisfaction >= 4.0) → Continue with remaining 5 user + 4 creator tests
- **If PIVOT signals** (GitHub barrier insurmountable, < 50% completion) → Test alternative UI (Kit Runner) in Week 9-10
- **If NO-GO signals** (satisfaction < 3.5, TTFW 30%+ over target) → Pause Phase 2; escalate to Phase-End Review

**Quick Fixes to Implement (Week 8)**:
- Copy changes (clearer instructions, tooltips)
- Reorder steps (if sequencing is confusing)
- Add video walkthrough (if GitHub OAuth is primary friction point)

#### Week 9 Checkpoint (Monday, End of Week 9)

**Check** (after 8 user + 6 creator tests):
- [ ] Did quick fixes improve metrics? (compare Week 7-8 vs Week 9 TTFW, satisfaction)
- [ ] User workflow: % completing in < 10 min? (target: 70%+)
- [ ] Creator workflow: % completing in < 5 min? (target: 80%+)
- [ ] Curation feedback: % rating 4+ stars even if rejected? (target: 70%+)
- [ ] Abandonment intent: % saying "I'd give up" after rejection? (target: < 10%)

**Act**:
- If improvements insufficient → Consider persona pivot (Eng Managers first, expand to PMs later)
- If curation satisfaction low → Refine feedback templates (provide examples of "good" vs "needs work")
- If abandonment high → Add auto-resubmit flow (one-click fix + resubmit)

#### Week 10 Checkpoint (Monday, End of Week 10)

**Check** (after 10 user + 8 creator tests):
- [ ] Phase 2 exit criteria met? (see below)
- [ ] Friction points documented + prioritized? (top 3 with fix roadmap)
- [ ] Participant pool recruited for Phase 3? (20+ beta testers from Phase 1 + Phase 2)

**Act**:
- If exit criteria met → Advance to Phase 3
- If exit criteria partially met → Extend Phase 2 by 1 week; conduct 2-3 additional tests with fixes
- If exit criteria not met → Escalate to Phase-End Review for pivot decision

---

### Phase 2 Exit Criteria (Go/Pivot/Kill Decision)

**GO Criteria** (all must pass):
- [ ] **User workflow completion**: 75%+ successfully complete workflow (fork kit + understand Quick Start)
- [ ] **User workflow TTFW**: 70%+ complete in < 10 min
- [ ] **User workflow satisfaction**: Avg satisfaction >= 4.0/5.0
- [ ] **Creator workflow completion**: 80%+ successfully submit kit
- [ ] **Creator workflow time**: 80%+ submit in < 5 min
- [ ] **Curation satisfaction**: 70%+ rate feedback 4+ stars (even if rejected)
- [ ] **Abandonment rate**: < 10% say "I'd give up" after rejection

**PIVOT Criteria**:
- [ ] **GitHub barrier insurmountable**: < 60% complete user workflow → Test Kit Runner web UI (no GitHub fork)
- [ ] **Persona mismatch**: Eng Managers 90% completion, Marketers 50% completion → Target technical users first
- [ ] **Curation friction**: Satisfaction < 3.5 stars → Explore automated quality checks before human review

**NO-GO/KILL Criteria**:
- [ ] **Workflow too complex**: < 50% completion after fixes
- [ ] **TTFW unachievable**: < 40% complete in < 10 min after optimizations
- [ ] **Satisfaction insufficient**: < 3.0 avg satisfaction after fixes
- [ ] **Abandonment high**: > 30% would give up after rejection

**Decision Owner**: Product + Design Leads
**Decision Date**: End of Week 10 (Monday)
**Decision Format**: Phase-End Review meeting (90 min)

---

## Phase 3: MVP Beta & Channel Validation (Weeks 11-16)

**Goal**: Launch curated MVP; validate network effects; identify highest-quality acquisition channel

### Weekly PDCA Checkpoints

#### Week 11-12 Checkpoints (Prep Weeks)

**Check** (end of Week 11):
- [ ] Seed kits created? (10-15 kits across 3+ domains: PM, Marketing, Legal)
- [ ] Founding creators recruited? (5-10 from Phase 1/2)
- [ ] PH launch assets ready? (video demo, screenshots, tagline, maker profile)
- [ ] Twitter threads + Reddit posts drafted?

**Act**:
- If seed kits < 10 → Prioritize creation; recruit more Phase 2 participants to contribute
- If PH assets incomplete → Extend prep to Week 13 Day 1 (delay launch by 2 days)

**Check** (end of Week 12):
- [ ] MVP deployed to kits.agentii.ai? (functional fork flow, submission flow)
- [ ] Analytics instrumented? (Vercel Analytics, GitHub API, UTM tracking)
- [ ] Beta testers recruited? (50+ from waitlist + Phase 1/2 participants)
- [ ] PH launch scheduled? (Week 13 Day 1, Tuesday 12:01am PST)

**Act**:
- If MVP not ready → Delay launch by 1 week; prioritize critical bugs
- If beta testers < 30 → Soft-launch to waitlist first (1 week early access)

#### Week 13 Checkpoint (Monday, End of Week 13) - **LAUNCH WEEK**

**Check** (Product Hunt launch + Twitter + Reddit executed):
- [ ] **PH**: Visits? ([X]), Upvotes? ([X], Top [X] product), Waitlist signups? ([X])
- [ ] **Twitter**: Impressions? ([X]), Clicks? ([X]), Signups? ([X])
- [ ] **Reddit**: Views? ([X]), Comments? ([X]), Signups? ([X])
- [ ] **Activation**: % who forked a kit within first session? ([X]% by channel)
- [ ] **Network effects**: Kit submissions from founders? ([X] new kits added)

**Act**:
- If PH underperforming (< 100 upvotes) → Engage community (respond to comments, thank upvoters)
- If activation < 10% → Revisit hero workflow (possible UX regression from MVP deploy)
- If no kit submissions → Reach out to founding creators (reminder + incentive)

#### Week 14 Checkpoint (Monday, End of Week 14)

**Check** (Content marketing launched):
- [ ] Blog posts published? (2 SEO-optimized guides: "How to X" targeting PM/marketing keywords)
- [ ] Organic traffic? ([X] visits from Google)
- [ ] Channel performance so far:
  - PH: Activation [X]%, D7 retention [X]%
  - Twitter: Activation [X]%, D7 retention [X]%
  - Reddit: Activation [X]%, D7 retention [X]%
  - Content: Activation [X]%, D7 retention [X]%

**Act**:
- If Content underperforming → Promote via Twitter/Reddit (cross-post links)
- If clear winner emerging → Double down (allocate remaining budget/effort)
- If all channels < 10% activation → Pause; revisit value prop or hero workflow

#### Week 15 Checkpoint (Monday, End of Week 15) - **ANALYSIS WEEK**

**Check** (Cohort analysis by channel):
- [ ] **Channel winner identified**? (activation × D7 retention score 2x+ better than second)
- [ ] **Network effects evident**? (R² > 0.6 for kit count → user signups correlation)
- [ ] **Cross-side conversion**? (X% of users submitted a kit within 30 days - target: 10%+)
- [ ] **Retention curves**: D7, D14, D30 by channel (plot + compare)

**Act**:
- If no clear winner → Extend Phase 3 by 1 week; test 2 additional channels (Paid Ads, SEO boost)
- If network effects weak (R² < 0.4) → Investigate: Are kits being shared socially? Add "Share" CTA
- If cross-side conversion low → Survey users: "Why haven't you submitted a kit?" (blockers?)

#### Week 16 Checkpoint (Monday, End of Week 16) - **FINAL WEEK**

**Check** (Phase 3 exit criteria):
- [ ] Activation 15%+ from at least 1 channel?
- [ ] D7 retention 30%+ from winner channel?
- [ ] Clear winner (2x better than second)?
- [ ] Network effects R² > 0.6?
- [ ] Cross-side conversion 10%+?
- [ ] 100+ activated users?
- [ ] 20+ kits live?

**Act**:
- If exit criteria met → Proceed to Phase-End Review for GO/SCALE decision
- If partially met → Document gaps; decide pivot vs continue
- If not met → Phase-End Review for NO-GO/PIVOT decision

---

### Phase 3 Exit Criteria (Go/Scale/Pivot Decision)

**GO Criteria** (all must pass):
- [ ] **Activation**: 15%+ from at least 1 channel
- [ ] **Retention**: D7 retention 30%+ from winner channel
- [ ] **Clear winner**: Combined score (activation × D7 retention) 2x+ better than second channel
- [ ] **Network effects**: R² > 0.6 for kit count → user signups correlation
- [ ] **Cross-side conversion**: 10%+ of users submit a kit within 30 days
- [ ] **Scale reached**: 100+ activated users; 20+ kits live

**SCALE Criteria** (ready for broader launch):
- [ ] All GO criteria met
- [ ] Winner channel repeatable (consistent over 2+ weeks)
- [ ] Acquisition playbook documented (audience, messaging, timing, format, budget)
- [ ] Creator pipeline healthy (5+ new kit submissions per week)

**PIVOT Criteria**:
- [ ] **No clear winner channel**: All channels < 15% activation → Revisit value prop; test alternative headlines
- [ ] **Network effects weak**: R² < 0.4 → Explore alternative models (SaaS subscription vs marketplace)
- [ ] **Single-side works**: Users engage but creators don't submit → Pivot to B2C SaaS (we curate, users consume)

**NO-GO Criteria** (kill hypothesis):
- [ ] **All channels fail**: Activation < 10% across all 4 channels
- [ ] **No retention**: D7 retention < 20% across all channels
- [ ] **No network effects**: R² < 0.3 (kits don't drive users)
- [ ] **Marketplace doesn't work**: Cross-side conversion < 5% (one-sided consumption only)

**Decision Owner**: Product + Growth Leads
**Decision Date**: End of Week 16 (Monday)
**Decision Format**: Phase-End Review meeting (90 min) + stakeholder presentation

---

## Weekly PMF Review Agenda (Every Monday, 10am EST)

**Duration**: 45 min
**Attendees**: Product Lead, Growth Lead, Design Lead, Community Manager (if Phase 3)

### Agenda Template

**1. Metrics Review (10 min)**

*Present latest numbers from Notion dashboard*

- **Phase 1**:
  - # interviews completed this week: [X] (total: [Y]/20)
  - Patterns emerging: [describe]
  - Quotes captured: [count]
  - JTBD mention rates: Discover [X]%, Share [X]%, Validate [X]%
  - Willingness-to-pay: [X]% willing to pay $[Y]/mo

- **Phase 2**:
  - # usability tests completed: User [X]/10, Creator [X]/8
  - TTFW progress: Median [X] min (target: < 10 min)
  - Completion rate: User [X]%, Creator [X]%
  - Satisfaction: User [X.X]/5.0, Creator [X.X]/5.0
  - Top 3 friction points: [list with counts]

- **Phase 3**:
  - Visits by channel: PH [X], Twitter [X], Reddit [X], Content [X]
  - Signups by channel: PH [X], Twitter [X], Reddit [X], Content [X]
  - Activation by channel: PH [X]%, Twitter [X]%, Reddit [X]%, Content [X]%
  - D7 retention by channel: PH [X]%, Twitter [X]%, Reddit [X]%, Content [X]%
  - Network effects: Kit count [X], User signups [X], R² [X.XX]
  - Cross-side conversion: [X]% of users → creators

**2. Learnings (15 min)**

*Discuss discoveries from this week*

- **What did we learn about personas, JTBD, workflows, or channels?**
  - Quote examples: "[Verbatim quote from interview/test]" - [Persona, JTBD]
  - Contradictory evidence: "[What doesn't fit our hypotheses?]"

- **Surprises**:
  - What did users say that we didn't expect?
  - What behavior did we observe that contradicts our assumptions?

- **Themes**:
  - Are patterns emerging across multiple participants?
  - Are friction points consistent or one-off issues?

**3. Blockers (10 min)**

*Identify issues slowing research*

- Participant no-shows: [X] this week - how to mitigate?
- Tool issues: Analytics not tracking? Zoom recording failed?
- Unclear findings: Do we need to adjust interview questions?
- Recruitment lag: Need more participants for next phase?

**4. Decisions Needed (5 min)**

*Flag decisions that require consensus*

- Should we pivot persona focus? (Eng Managers showing stronger signals than PMs)
- Should we adjust interview questions? (Current questions not surfacing willingness-to-pay)
- Should we test alternative UI? (GitHub barrier higher than expected)
- Should we extend phase? (Need 5 more interviews to saturate patterns)

**5. Next Week Focus (5 min)**

*Assign tasks and set priorities*

- **Do (next week)**:
  - Phase 1: Conduct [X] interviews (Creator: [X], User: [X])
  - Phase 2: Run [X] usability tests (User: [X], Creator: [X])
  - Phase 3: Execute [channel] launch; monitor daily metrics

- **Assignments**:
  - [Name]: Interview [participants], synthesize quotes in Notion
  - [Name]: Conduct usability tests, record TTFW + friction points
  - [Name]: Monitor channel performance, prepare cohort analysis

**Output**: Updated Notion dashboard + task assignments + pivot decisions documented

---

## Phase-End Review Agenda (Every 4 Weeks, End of Phase)

**Duration**: 90 min
**Attendees**: Product Lead, Stakeholders (founder, advisors if any), Growth/Design Leads

### Agenda Template

**1. Phase Summary (20 min)**

*Present consolidated findings*

- **Phase 1**: Persona + JTBD validation
  - Show: Persona profiles with quotes
  - Show: JTBD mention rates (P1, P2, P3)
  - Show: Willingness-to-pay summary (% willing, price thresholds)
  - Show: Incumbent pain points (PromptBase, Notion, ChatGPT gaps)

- **Phase 2**: Hero workflow validation
  - Show: TTFW distribution (user workflow: min, median, max)
  - Show: Completion rates (user [X]%, creator [X]%)
  - Show: Satisfaction scores (user [X.X]/5.0, creator [X.X]/5.0)
  - Show: Top 3 friction points with fix roadmap

- **Phase 3**: Channel + network effects validation
  - Show: Channel performance table (activation, retention, combined score)
  - Show: Network effects scatter plot (kit count → user signups, R² = [X.XX])
  - Show: Cross-side conversion (X% users → creators)
  - Show: Cohort retention curves (D7, D14, D30 by channel)

**2. Exit Criteria Review (30 min)**

*Compare findings to thresholds*

- **Does this phase meet GO criteria?**
  - Phase 1: 70%+ pain frequency ✅/❌, 60%+ willingness-to-try ✅/❌, 40%+ willingness-to-pay ✅/❌
  - Phase 2: 75%+ completion ✅/❌, 70%+ TTFW < 10 min ✅/❌, 4.0+ satisfaction ✅/❌
  - Phase 3: 15%+ activation ✅/❌, 30%+ D7 retention ✅/❌, clear winner ✅/❌, R² > 0.6 ✅/❌

- **Decision Options**:
  - **GO**: All criteria met → Advance to next phase (or SCALE if Phase 3)
  - **PIVOT**: Some criteria met, but adjustments needed → What do we change? Re-run phase or skip to Phase 3?
  - **NO-GO**: Criteria not met → Kill hypothesis; explore alternative personas, JTBD, or business models

**3. Next Phase Planning (40 min)**

*If GO decision, plan next phase*

- **Phase 2 Planning** (if advancing from Phase 1):
  - Review hero workflows to test (user workflow, creator workflow)
  - Assign owners: Product + Design Leads
  - Set timeline: 4 weeks (Weeks 7-10)
  - Budget: $900 (18 usability tests × $50)
  - Dependencies: Need Figma mockups? Need MVP deployed?

- **Phase 3 Planning** (if advancing from Phase 2):
  - Review MVP scope: Seed kits, founding creators, channel sequence
  - Assign owners: Growth + Product Leads
  - Set timeline: 6 weeks (Weeks 11-16)
  - Budget: $500 (paid promotion if needed)
  - Dependencies: MVP deploy, PH launch assets, beta tester recruitment

- **Scale Planning** (if Phase 3 GO/SCALE):
  - Document acquisition playbook (winner channel: audience, messaging, timing, format)
  - Plan broader launch (expand to more channels, recruit more creators, build automation)
  - Budget: [X] for scaling (paid ads, creator incentives, tooling)
  - Hiring: Do we need Growth Marketer? Community Manager?

**Output**: GO/PIVOT/NO-GO decision documented + next phase plan approved (or pivot strategy if not GO)

---

## Summary: Validation Checkpoints Alignment

All checkpoints trace back to constitution principles:

- **Iterative Validation** (Principle): Independent PDCA cycles at Phase 1, 2, 3 with explicit go/kill/pivot gates ✅
- **Minimal Viable Process** (Principle): Qualitative → quantitative; manual before automated; smallest experiments sequenced ✅
- **Customer-Evidence-Driven** (Principle): All checkpoints measure direct evidence (interviews, usability tests, behavioral analytics) ✅
- **Measurable Learning Velocity** (Principle): Weekly reviews + phase-end decisions enable fast pivots ✅

All decisions are traceable to research questions (research-questions.md) and PMF spec hypotheses (spec.md).
