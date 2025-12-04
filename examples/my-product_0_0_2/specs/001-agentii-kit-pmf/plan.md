# PMF Research Plan: agentii-kit Website

**Feature Branch**: `001-agentii-kit-pmf`
**Created**: 2025-12-04
**Status**: Draft
**Discovery Phase**: Phase 0: Foundations

---

## Research Context *(mandatory)*

### Primary Research Questions

**Question 1**: Do our target personas (Kit Creators and Kit Users) actually have the JTBD we think they do with sufficient frequency and pain intensity to warrant a new solution?

- **Hypothesis**: PMs and marketers spend 2+ hours per week on workflow setup (PRDs, campaign briefs) using copy-paste/ChatGPT workarounds; they actively seek structured templates
- **Success threshold**: 70%+ of interviewed personas report 2+ hours/week on workflow setup; 60%+ mention actively searching for "templates," "automation," or "AI workflows"
- **Evidence source**: In-depth interviews (45-60 min, N=20 split 10 creators + 10 users)

**Question 2**: Is there genuine willingness-to-pay for kit marketplace value (quality curation, GitHub integration, version control) vs. free alternatives (Google search, PromptBase, Notion templates)?

- **Hypothesis**: Users and creators value community-curated, GitHub-native kits enough to choose agentii-kit over incumbent free alternatives
- **Success threshold**: 80%+ mention specific incumbent pain points (low quality, no updates, static templates); 50%+ indicate they'd pay $5-20/mo for premium features (future state)
- **Evidence source**: Willingness-to-pay probes in interviews; landing page conversion rate (waitlist signups as demand signal)

**Question 3**: Can Kit Users (non-technical PMs/marketers) realistically complete the "Discover and Fork a Kit" hero workflow in < 10 minutes with acceptable satisfaction?

- **Hypothesis**: With GitHub OAuth + one-click fork + video walkthrough, non-technical users can complete workflow successfully
- **Success threshold**: 75%+ of non-technical test users (N=10) complete workflow in < 10 min; satisfaction >= 4/5 stars
- **Evidence source**: Moderated usability testing sessions with PM/marketer participants (not engineers)

**Question 4**: Can Kit Creators complete the "Submit and Share a Kit" workflow in < 5 minutes, and does manual curation (24-48 hour turnaround) meet acceptable quality standards without killing creator motivation?

- **Hypothesis**: Manual curation enables quality control while maintaining creator satisfaction; < 5 min submission time acceptable
- **Success threshold**: 80%+ of test creators (N=8) complete submission in < 5 min; 70%+ rate curation feedback 4+ stars (even if rejected); < 10% abandonment rate after rejection
- **Evidence source**: Creator workflow usability tests + post-curation satisfaction survey

**Question 5**: Does the two-sided marketplace exhibit network effects? Do more kits drive more users, and do more users incentivize more creators?

- **Hypothesis**: Each new kit submission drives 5+ new users (social sharing, SEO); 10%+ of users convert to creators within 30 days
- **Success threshold**: Measurable correlation (R² > 0.6) between kit count and user signups; cross-side conversion rate 10%+
- **Evidence source**: Behavioral analytics during Phase 3 beta launch; track kit submission events → user signup spikes

**Question 6**: Which distribution channel (Product Hunt, Twitter, Reddit, Content) delivers the highest-quality users (activated, retained, referring)?

- **Hypothesis**: Product Hunt drives highest volume but Reddit/communities drive highest quality (D7 retention 40%+ vs PH 25%)
- **Success threshold**: Identify 1-2 channels with activation 15%+ AND D7 retention 30%+; clear winner with 2x better combined metric
- **Evidence source**: Multi-channel beta launch with UTM tracking → cohort analysis by source

---

### Research Phases & Exit Criteria

Research progresses through PDCA cycles (Plan → Do → Check → Act) at 2-4 week intervals.

**Phase 0 – Foundations** (2 weeks): Constitution complete ✅, PMF spec complete ✅, recruit participant pipeline, create research instruments
**Phase 1 – Persona & Problem Validation** (4 weeks): 20 interviews (10 creators, 10 users); personas + JTBD confirmed; willingness-to-pay signals captured
**Phase 2 – Hero Workflow Validation** (4 weeks): 18 usability tests (10 user workflow, 8 creator workflow); TTFW targets met; GitHub barrier mitigated
**Phase 3 – MVP Beta & Channel Validation** (6 weeks): Launch curated MVP with 10-15 seed kits; test 3 channels; 100+ activated users; network effects measured

---

## Constitution Check *(mandatory)*

Verify alignment with agentii-kit constitution principles (.specify/memory/constitution.md):

- [x] **Principle I: Two-Sided Marketplace Validation**: Research questions split between creators (Q1, Q4) and users (Q1, Q3); success metrics track both supply and demand health (Q5)
- [x] **Principle II: Community-First Discovery**: Direct interviews prioritized (Q1, Q2); qualitative satisfaction scores required (Q3, Q4); verbatim quotes captured
- [x] **Principle III: Content Quality Over Quantity**: Manual curation validation built into research design (Q4); quality rubric tested with creators
- [x] **Principle IV: GitHub-Native Distribution**: Hero workflow tests specifically validate GitHub fork flow (Q3); no proprietary workarounds
- [x] **Principle V: Progressive Disclosure**: Non-technical user testing validates complexity abstraction (Q3); tiered experience tested
- [x] **Principle VI: Measurable Learning Velocity**: Landing page (Q2) before MVP (Q3); manual curation (Q4) before automation; smallest experiments sequenced
- [x] **Principle VII: Monetization-Aware Architecture**: Willingness-to-pay probes included (Q2); premium feature preferences explored without commitment

**Methodology Validation**:
- ✅ Specification-First: All research questions directly traceable to PMF spec hypotheses (spec.md lines 327-331 Open Questions, lines 72-118 JTBD)
- ✅ Customer-Evidence-Driven: Direct interviews (N=20), usability tests (N=18), behavioral analytics (Phase 3); no proxy metrics
- ✅ Iterative Validation: Independent PDCA cycles at Phase 1, 2, 3; explicit go/kill/pivot gates
- ✅ Minimal Viable Process: Qualitative (interviews) before quantitative (analytics); manual curation before automation; landing page before app
- ✅ Cross-Functional: Research spans product (JTBD), design (usability), growth (channels), community (curation)

---

## Phase 0: Foundations (Weeks 1-2)

**Goal**: Prepare research infrastructure and recruit participant pipeline before Phase 1 interviews

**Duration**: 2 weeks | **Owner**: Product Lead

**Activities**:

1. **Finalize Research Instruments** (Week 1):
   - Draft interview guide for creators and users (see research-instruments.md)
   - Draft usability testing scripts for both hero workflows
   - Create post-session satisfaction survey (1-5 star ratings + open-ended)
   - Draft landing page copy for demand validation

2. **Recruit Participant Pipeline** (Week 1-2):
   - **Creators** (target N=10 for Phase 1):
     - Source from: Twitter (#PMLife, #ProductManagement), LinkedIn (PM groups), r/ProductManagement
     - Criteria: Senior PM or Marketing Lead at Series A-B SaaS, 3+ years experience, uses AI agents (Claude/ChatGPT)
     - Incentive: $50 Amazon gift card per 60-min interview
   - **Users** (target N=10 for Phase 1):
     - Source from: Reddit (r/marketing, r/GrowthHacking), Indie Hackers, Twitter (#GrowthMarketing)
     - Criteria: Growth marketer or PM at seed-Series A, 2+ years experience, uses AI for work
     - Incentive: $50 Amazon gift card per 60-min interview
   - Recruitment method: Direct DMs + screener survey (Google Form) to qualify

3. **Instrument Analytics** (Week 2):
   - Set up Vercel Analytics on landing page (track visits, UTM sources, waitlist signups)
   - Create Typeform for waitlist (email + role + "What problem are you trying to solve?")
   - Set up GitHub API access for future kit tracking (forks, stars, issues)
   - Create Notion dashboard for interview synthesis (personas, quotes, JTBD evidence)

4. **Create Landing Page** (Week 2):
   - Purpose: Validate demand before building
   - Content: Value prop headline, 3 kit category examples (PM, Marketing, Legal), "Join Waitlist" CTA, GitHub social proof
   - Deploy to: kits.agentii.ai (Vercel)
   - Success metric: 100+ waitlist signups from organic/paid traffic (baseline demand signal)

**Phase 0 Exit Criteria**:
- [ ] 20+ qualified participants recruited (10 creators, 10 users)
- [ ] Research instruments finalized and reviewed
- [ ] Landing page live with analytics instrumented
- [ ] Notion synthesis dashboard set up

---

## Phase 1: Persona & Problem Validation (Weeks 3-6)

**Goal**: Confirm personas and JTBD are real, urgent, and worth solving for BOTH creators and users

**Duration**: 4 weeks | **Owner**: Product Lead

### Research Activities

**In-Depth Interviews**: N=20 (10 creators, 10 users)
- Duration: 45-60 min per interview (remote, recorded via Zoom with consent)
- Cadence: 4-5 interviews per week
- Topics:
  1. Role/context establishment (tools, team, success metrics)
  2. Current workflow for JTBD (PRD writing, campaign briefs, etc.)
  3. Pain frequency and intensity (hours spent, frustration points)
  4. Current workarounds (copy-paste, templates, AI prompts)
  5. Willingness-to-try new solution (what would make it worth their time?)
  6. Competitive alternatives awareness (PromptBase, Notion, Cursor Rules)
  7. Willingness-to-pay signals (would you pay? how much? for what?)

**Evidence Collection Instrument**: See `research-instruments.md` for full interview guide

### Weekly PDCA (4-week cycle)

**Week 3-4 (Do)**:
- Conduct 8-10 interviews (mix creators + users)
- Synthesize quotes in Notion (tag by persona, JTBD, pain intensity)

**Week 4 Check**:
- After 10 interviews: Are patterns emerging? Do personas feel distinct?
- Are JTBD frequencies matching hypothesis (2+ hours/week)?
- Are willingness-to-pay signals present (mentions of "would pay," "switch from X")?
- If NO clear patterns → Adjust interview questions or pivot persona definitions

**Week 5-6 (Do + Act)**:
- Conduct remaining 10 interviews with revised questions (if needed)
- Finalize persona profiles with verbatim quotes
- Validate JTBD priority (P1, P2, P3) based on mention frequency
- Document willingness-to-pay evidence (quotes, price sensitivity)

### Phase 1 Exit Criteria (Go/No-Go Decision)

- [ ] **GO**: 70%+ of creators report spending 2+ hours/week on workflow setup (PRD/campaign briefs); 60%+ actively search for templates/automation
- [ ] **GO**: 70%+ of users report same pain frequency; 50%+ mention trying PromptBase/Notion/ChatGPT and finding gaps
- [ ] **GO**: Willingness-to-try signal evident (60%+ say "I'd try this immediately" or equivalent enthusiasm)
- [ ] **GO**: Willingness-to-pay signals present (40%+ indicate they'd pay $5-20/mo for premium features)
- [ ] **NO-GO**: Pain signals weak (< 50% report 2+ hrs/week); explore adjacent personas (e.g., Legal Ops, Educators)
- [ ] **PIVOT**: Different JTBD emerges as higher priority (e.g., "collaboration on kits" > "discovering kits"); refocus spec

### Successful Phase 1 Output

- Validated persona profiles (2-3 primary) with role, pain, frequency, willingness-to-try
- Top 3 JTBD with evidence:
  - JTBD #1: "Discover Proven Workflows" (mention rate, quote examples)
  - JTBD #2: "Share My Workflow" (mention rate, motivation signals)
  - JTBD #3: "Validate Kit Quality" (mention rate, quality criteria)
- Willingness-to-pay summary:
  - % willing to pay
  - Price sensitivity ($0, $5/mo, $20/mo thresholds)
  - Premium features mentioned (private kits, advanced search, creator monetization)
- Participant pool for Phase 2 usability testing (recruit from Phase 1 interviewees)

---

## Phase 2: Hero Workflow Validation (Weeks 7-10)

**Goal**: Ensure both hero workflows deliver value and users can execute end-to-end; validate TTFW targets and GitHub barrier mitigation

**Duration**: 4 weeks | **Owner**: Product + Design

### Research Activities

**Usability Testing – User Workflow** ("Discover and Fork a Kit"): N=10
- Duration: 45 min per session (moderated, remote via Zoom)
- Participants: PM/marketer personas from Phase 1 (non-technical)
- Setup:
  - Provide scenario: "You need to write a marketing campaign brief for a product launch. Find a kit that helps."
  - Ask them to complete: Browse homepage → Search/filter → Select kit → Fork to GitHub → View Quick Start guide
  - Think-aloud protocol: Narrate what they're doing, what's confusing, what's easy
- Measures:
  - TTFW (time from landing page to successful fork): Target < 10 min
  - Task completion rate: Target 75%+
  - Friction points: Where do they get stuck? (no GitHub account, unclear instructions, etc.)
  - Satisfaction: Post-session 1-5 star rating; Target >= 4.0 avg

**Usability Testing – Creator Workflow** ("Submit and Share a Kit"): N=8
- Duration: 45 min per session
- Participants: PM/marketer personas from Phase 1 who have created templates before
- Setup:
  - Provide scenario: "You've created a PM PRD template you want to share. Submit it to agentii-kit."
  - Ask them to complete: Click "Submit a Kit" → GitHub OAuth → Select repo → Fill metadata → Preview card → Submit
  - Simulate manual review: Show example rejection feedback ("Missing example use case") and acceptance notification
- Measures:
  - Time to submission: Target < 5 min (excluding review wait)
  - Task completion rate: Target 80%+
  - Curation feedback satisfaction: 4+ stars even if rejected (test feedback quality)
  - Abandonment after rejection: Target < 10%

**Evidence Collection Instrument**: See `research-instruments.md` for usability testing scripts

### Weekly PDCA (4-week cycle)

**Week 7-8 (Do)**:
- Conduct 5 user workflow tests + 4 creator workflow tests
- Tag friction points in Notion (categorize: GitHub barrier, unclear copy, missing feature, etc.)

**Week 8 Check**:
- Are TTFW targets being met? If not, where are delays?
- Are non-technical users struggling with GitHub fork? → Test "Quick Start Video" mitigation
- Is manual curation feedback perceived as helpful or frustrating? → Refine feedback template

**Week 9-10 (Act)**:
- Make quick non-technical fixes (copy changes, reorder steps, add tooltips)
- Conduct remaining 5 user + 4 creator tests with fixes applied
- Measure improvement: Did friction points reduce? Did satisfaction scores increase?

### Phase 2 Exit Criteria (Go/Kill/Pivot)

- [ ] **GO**: 75%+ of users complete workflow successfully; TTFW < 10 min achieved by 70%+; satisfaction >= 4.0
- [ ] **GO**: 80%+ of creators complete submission in < 5 min; curation feedback rated 4+ stars by 70%+
- [ ] **NO-GO**: Workflow too complex (< 50% completion); GitHub barrier insurmountable; redesign required
- [ ] **PIVOT**: Workflow works for Persona A (Eng Managers) but not Persona B (Marketers) → shift focus to technical users first
- [ ] **PIVOT**: Manual curation satisfaction < 3.5 stars → explore automated quality checks before human review

### Successful Phase 2 Output

- Usability test summary:
  - User workflow: TTFW distribution (min, median, max), completion rate, friction points prioritized
  - Creator workflow: Submission time, completion rate, curation feedback themes
- Quotes:
  - Positive: "Wow, that was way easier than I expected" (validate GitHub OAuth works)
  - Negative: "I got stuck at [step]" (prioritize fix for Phase 3)
- Friction point fixes implemented (or roadmap if requires dev work)
- Participant pool for Phase 3 beta testing (recruit Phase 2 participants + Phase 1 interviewees)

---

## Phase 3: MVP Beta & Channel Validation (Weeks 11-16)

**Goal**: Launch curated MVP with 10-15 seed kits; validate network effects; identify highest-quality acquisition channel

**Duration**: 6 weeks | **Owner**: Growth + Product

### Research Activities

**MVP Beta Launch**:
- **Seed Supply** (Week 11-12):
  - Manually create 10-15 high-quality kits (PM-Kit, Marketing-Kit, Legal-Kit, Edu-Kit)
  - Recruit 5-10 "founding creators" from Phase 1/2 to submit kits pre-launch
  - Ensure diversity: 3+ domains (PM, Marketing, Legal), 2+ kits per domain
- **Launch Sequence** (Week 13):
  - Week 13 Day 1: Product Hunt launch (primary channel)
  - Week 13 Day 3: Twitter thread series (secondary channel)
  - Week 13 Day 5: Reddit posts (r/ProductManagement, r/marketing) (secondary channel)
  - Week 14-16: Content marketing (publish 2-3 SEO-optimized guides) (tertiary channel)

**Channel Testing**:
- Measure for EACH channel:
  - **Top of funnel**: Visits, UTM-tagged signups
  - **Activation**: % who fork a kit within first session
  - **Engagement**: % who fork 2+ kits within 7 days
  - **Retention**: Day-7 and Day-30 return visitor rate
  - **Referral**: % who invite a colleague (track via referral links)
- Tools: Vercel Analytics + GitHub API + Typeform surveys

**Network Effects Measurement**:
- Track: Kit submission events → spike in user signups (7-day window)
- Track: User cohort → % who submit a kit within 30 days (cross-side conversion)
- Hypothesis validation: Does each new kit drive 5+ new users? (Q5 from Research Questions)

### Weekly PDCA (6-week cycle)

**Week 11-12 (Prep)**:
- Create seed kits, recruit founding creators
- Finalize PH launch assets (video demo, screenshots, tagline)
- Prepare Twitter threads and Reddit posts

**Week 13-14 (Launch + Monitor)**:
- Execute channel launches sequentially
- Track daily: Visits, signups, activations by channel
- Identify: Which channel drives highest activation? Lowest CAC?

**Week 15 (Check)**:
- Cohort analysis: Activation rate, D7 retention by channel
- Network effects: Kit count → user signup correlation (plot scatter, calculate R²)
- Decision: Which channel is the winner (2x better than second place)?

**Week 16 (Act)**:
- Double down on winner channel (allocate remaining budget/effort)
- Kill low-performing channels (< 10% activation or < 20% D7 retention)
- Document acquisition playbook for winner channel (audience, messaging, timing, format)

### Phase 3 Exit Criteria (Go/Scale/Pivot)

- [ ] **GO**: Activation 15%+, D7 retention 30%+ from at least 1 channel
- [ ] **GO**: Network effects evident (R² > 0.6 for kit count → user signups; 10%+ cross-side conversion)
- [ ] **SCALE**: Clear winner channel identified (2x better than second); 100+ activated users; 20+ kits live
- [ ] **PIVOT**: Activation < 10% across all channels → revisit value prop, hero workflow, or target persona
- [ ] **PIVOT**: Network effects weak (R² < 0.4) → marketplace may not work; explore alternative model (SaaS, content site)

### Successful Phase 3 Output

- Channel performance summary:
  - Product Hunt: 500+ visits, 15% activation, 25% D7 retention, $X CAC
  - Twitter: 300+ visits, 20% activation, 35% D7 retention, $Y CAC
  - Reddit: 200+ visits, 12% activation, 40% D7 retention, $Z CAC
  - Winner: Twitter (highest combined activation × retention score)
- Network effects analysis:
  - Kit count vs user signups: R² = 0.72 (strong correlation)
  - Cross-side conversion: 12% of users submitted a kit within 30 days
  - Conclusion: Marketplace dynamics validated ✅
- Cohort retention curves:
  - By channel: Show D7, D14, D30 retention by acquisition source
  - By persona: Kit Creators vs Kit Users retention comparison
- Acquisition playbook:
  - Winner channel: Twitter
  - Audience: PM/marketing communities (#PMLife, #GrowthMarketing)
  - Messaging: Problem-solution storytelling (before/after kit adoption)
  - Format: Tweet threads (8-10 tweets) with demo screenshots
  - Timing: Tuesday/Wednesday 10am-12pm EST (highest engagement)
  - Budget: $500/mo for promoted tweets (if needed)
- Go/no-go decision on scaling:
  - **If GO**: Proceed to broader launch (expand to more channels, recruit more creators, build automation)
  - **If PIVOT**: Document learnings, adjust strategy, retest

---

## Validation Checkpoints & Rituals

### Weekly PMF Review (Every Monday, 10am EST)

**Attendees**: Product Lead, Growth Lead, Design Lead, Community Manager (if Phase 3)
**Duration**: 45 min

**Agenda**:
1. **Metrics Review** (10 min):
   - Phase 1: # interviews completed, patterns emerging, quotes captured
   - Phase 2: # usability tests completed, TTFW progress, friction points
   - Phase 3: Visits, signups, activations, retention by channel
2. **Learnings** (15 min):
   - What did we discover this week about personas, JTBD, workflows, or channels?
   - Verbatim quotes: What did users say that surprised us?
   - Contradictory evidence: What doesn't fit our hypotheses?
3. **Blockers** (10 min):
   - What's slowing research? (participant no-shows, tool issues, unclear findings)
   - Decisions needed: Should we adjust interview questions? Pivot persona focus?
4. **Next Week Focus** (10 min):
   - What's the PDCA "Do" for next week?
   - Task assignments: Who's doing what by when?

**Output**: Updated Notion dashboard + task priorities + any pivot decisions documented

### Phase-End Review (Every 4 Weeks, End of Phase)

**Attendees**: Product Lead, Stakeholders (founder, advisors if any)
**Duration**: 90 min

**Agenda**:
1. **Phase Summary** (20 min):
   - Present findings: Quotes, data, synthesis
   - Compare to hypotheses: What was validated? What was invalidated?
2. **Exit Criteria Review** (30 min):
   - Does this phase meet GO thresholds?
   - If YES → Decision: Advance to next phase (budget, timeline, scope)
   - If PIVOT → Decision: What do we adjust? Re-run phase or skip to Phase 3?
   - If NO-GO → Decision: Kill hypothesis; explore alternative personas or JTBD
3. **Next Phase Planning** (40 min):
   - Review next phase research questions and activities
   - Assign owners, set deadlines, allocate budget
   - Identify dependencies (e.g., need design mockups for Phase 2 usability tests)

**Output**: Go/Pivot/No-Go decision documented + next phase plan approved

---

## Success Criteria Summary

| Phase | Research Question | Success Metric | Go Threshold |
|-------|------------------|----------------|--------------|
| **1: Problem** | Do personas have JTBD? | % mentioning 2+ hrs/week pain | 70%+ |
| **1: Problem** | Willingness to try? | % expressing enthusiasm | 60%+ |
| **1: Problem** | Willingness to pay? | % indicating $5-20/mo acceptable | 40%+ |
| **2: Workflow (User)** | Can users complete workflow? | Task completion rate | 75%+ |
| **2: Workflow (User)** | TTFW < 10 min? | % completing in < 10 min | 70%+ |
| **2: Workflow (User)** | Satisfaction? | Avg 1-5 rating | >= 4.0 |
| **2: Workflow (Creator)** | Can creators submit kit? | Task completion rate | 80%+ |
| **2: Workflow (Creator)** | Submission < 5 min? | % completing in < 5 min | 80%+ |
| **2: Workflow (Creator)** | Curation satisfaction? | Avg 1-5 rating (even if rejected) | >= 4.0 |
| **3: Channel** | Which channel works? | Activation rate | 15%+ |
| **3: Channel** | Retention? | Day-7 retention | 30%+ |
| **3: Channel** | Clear winner? | Activation × Retention score | 2x+ vs 2nd place |
| **3: Network Effects** | Kits → Users correlation | R² for kit count → signups | > 0.6 |
| **3: Network Effects** | Cross-side conversion | % users → creators in 30 days | 10%+ |

---

## Risk Mitigation & Contingency Plans

### Risk 1: Participant Recruitment Fails (< 10 interviews in Phase 1)

**Mitigation**:
- Increase incentive: $50 → $75 gift card
- Expand sourcing: Add LinkedIn PM groups, Indie Hackers forums
- Leverage network: Ask Phase 1 participants for referrals (snowball sampling)
- Fallback: Extend Phase 1 by 2 weeks; accept N=15 instead of N=20 if patterns saturate

### Risk 2: GitHub Barrier Insurmountable (< 50% completion in Phase 2)

**Mitigation**:
- Test alternative: Create "Kit Runner" web UI prototype (no GitHub fork required)
- Hypothesis: If web UI improves completion to 75%+, pivot to web-first experience
- Trade-off: Higher dev cost, but lower user friction → validate with A/B test in Phase 3
- Fallback: Target Eng Managers first (GitHub-fluent), expand to PMs later

### Risk 3: No Clear Winner Channel (All < 15% activation in Phase 3)

**Mitigation**:
- Extend Phase 3 by 2 weeks; test 2 additional channels (Content SEO, Paid Ads)
- Revisit value prop: Is messaging off? Test alternative headlines on landing page
- Pivot hypothesis: Maybe direct sales (outbound to PMs) works better than PLG
- Fallback: If no channel works, revisit JTBD validation from Phase 1 → possible false positive

### Risk 4: Network Effects Don't Materialize (R² < 0.4 in Phase 3)

**Mitigation**:
- Investigate: Are kits being shared socially? Are creators promoting submissions?
- Test: Add explicit "Share this kit" CTA + Twitter card previews
- Pivot: If network effects weak, explore alternative models:
  - Option A: SaaS tool (not marketplace) - users subscribe, we curate
  - Option B: Content site (affiliate model) - monetize via ads/sponsors
- Fallback: If marketplace model fails, pivot to single-side model (B2C SaaS for users only)

---

## Next Steps

### Immediate (This Week)

1. ✅ **Constitution complete** (.specify/memory/constitution.md) - DONE
2. ✅ **PMF spec complete** (specs/001-agentii-kit-pmf/spec.md) - DONE
3. ✅ **Research plan complete** (specs/001-agentii-kit-pmf/plan.md) - DONE (this file)
4. [ ] **Generate research instruments** → Run research-instruments.md generation (Phase 0 artifact)
5. [ ] **Generate validation checkpoints** → Run validation-checkpoints.md generation (Phase 0 artifact)
6. [ ] **Update agent context** → Run `.specify/scripts/bash/update-agent-context.sh` to add research methodology

### Phase 0 Kickoff (Next 2 Weeks)

1. [ ] Finalize research instruments (interview guides, usability scripts, surveys)
2. [ ] Recruit 20 participants (10 creators, 10 users) via Twitter/Reddit/LinkedIn
3. [ ] Create landing page + deploy to kits.agentii.ai (Vercel)
4. [ ] Set up analytics (Vercel Analytics, GitHub API, Typeform, Notion dashboard)
5. [ ] Launch landing page + soft promotion (Twitter, Reddit) to gather baseline demand signal

### Phase 1 Launch (Week 3)

1. [ ] Begin interviews (4-5 per week for 4 weeks)
2. [ ] Weekly PDCA reviews (Mondays 10am)
3. [ ] Synthesize findings in Notion (quotes, JTBD evidence, willingness-to-pay)
4. [ ] Phase 1 exit criteria review (end of Week 6) → Go/Pivot/No-Go decision

**Tools Needed**:
- Zoom (interviews + usability tests)
- Calendly (scheduling)
- Notion (synthesis dashboard)
- Typeform (landing page waitlist + post-session surveys)
- Vercel Analytics (landing page traffic)
- GitHub API (future kit tracking in Phase 3)
- Figma (mockups for Phase 2 usability tests - if needed)

**Budget Estimate**:
- Phase 1: 20 interviews × $50 = $1,000 (participant incentives)
- Phase 2: 18 usability tests × $50 = $900
- Phase 3: $500 (paid promotion if needed - Product Hunt, Twitter ads)
- **Total**: ~$2,400 for Phases 1-3 research

---

## Appendix: Research Artifact Index

Generated research artifacts (to be created in next steps):

1. **research-questions.md**: Detailed breakdown of 6 primary research questions with hypotheses, validation approaches, and success thresholds
2. **research-instruments.md**: Full interview guides (creator + user), usability testing scripts (user workflow + creator workflow), post-session survey templates
3. **validation-checkpoints.md**: PDCA cycle gates for each phase with go/kill/pivot criteria, weekly review agendas, phase-end decision frameworks

These artifacts will be generated in the next command execution and stored in:
- `specs/001-agentii-kit-pmf/research-questions.md`
- `specs/001-agentii-kit-pmf/research-instruments.md`
- `specs/001-agentii-kit-pmf/validation-checkpoints.md`
