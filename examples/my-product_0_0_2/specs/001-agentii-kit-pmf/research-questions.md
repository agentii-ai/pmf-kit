# Research Questions: agentii-kit PMF Discovery

**Feature**: 001-agentii-kit-pmf
**Created**: 2025-12-04
**Status**: Active Research

---

## Overview

This document operationalizes the 6 primary research questions from plan.md into testable hypotheses with clear validation approaches and success thresholds. Each question maps to specific phases of the research plan and contributes to the overall PMF validation decision.

---

## Question 1: Persona & JTBD Validation

**Research Question**: Do our target personas (Kit Creators and Kit Users) actually have the JTBD we think they do with sufficient frequency and pain intensity to warrant a new solution?

### Hypothesis

**H1.1**: Senior PMs and Marketing Leads spend 2+ hours per week on workflow setup (writing PRDs, campaign briefs, etc.) using inefficient workarounds (copy-paste from old work, ChatGPT with ad-hoc prompts, static Notion templates).

**H1.2**: They actively seek structured templates and automation, evidenced by searches for "PM templates," "PRD automation," "marketing workflow," "AI for product managers."

**H1.3**: Personas feel distinct pain in three core JTBD:
- P1: Discover Proven Workflows (most frequent, weekly to monthly)
- P2: Share My Workflow (less frequent, quarterly to annually)
- P3: Validate Kit Quality (every discovery event)

### Validation Approach

**Phase**: Phase 1 - Persona & Problem Validation (Weeks 3-6)

**Method**: In-depth interviews with N=20 participants (10 Kit Creators, 10 Kit Users)

**Interview Protocol**:
1. Screen for persona fit: Role, company stage, tools used, AI agent familiarity
2. Current workflow deep-dive: "Walk me through how you currently [write PRDs / create campaign briefs]"
3. Pain frequency probe: "How often do you do this? How long does it take?"
4. Workaround exploration: "What tools/templates do you use? What's frustrating about them?"
5. JTBD validation: "When you're starting a new [feature/campaign], what's the first thing you do?"
6. Active search behavior: "Have you searched for templates or automation for this? What did you try?"

**Evidence Collection**:
- Verbatim quotes tagged by persona, JTBD, pain intensity
- Frequency counts: % mentioning each JTBD unprompted
- Time spent: Hours per week reported (median, range)
- Workaround mentions: PromptBase, Notion, ChatGPT, Google Docs (count by tool)

### Success Threshold

**GO Criteria** (all must pass):
- **H1.1 Validated**: 70%+ of creators report spending 2+ hours/week on workflow setup
- **H1.1 Validated**: 70%+ of users report same pain frequency
- **H1.2 Validated**: 60%+ mention actively searching for "templates," "automation," or "AI workflows" (exact keywords)
- **H1.3 Validated**: JTBD #1 (Discover) mentioned by 80%+; JTBD #2 (Share) mentioned by 50%+; JTBD #3 (Validate) mentioned by 70%+

**NO-GO Criteria**:
- Pain signals weak: < 50% report 2+ hours/week
- No active search behavior: < 40% mention seeking templates/automation
- JTBD mismatch: Different job emerges as primary (e.g., "collaborate on kits" > "discover kits")

**Pivot Criteria**:
- Adjacent persona stronger: Eng Managers (already Spec-Kit users) show 90%+ pain vs 60% for PMs
- Different domain: Legal Ops or Educators report higher pain/frequency than PM/Marketing

**Metrics Collected**:
| Metric | Target | Measurement |
|--------|--------|-------------|
| % mentioning 2+ hrs/week pain | 70%+ | Interview count / total |
| % actively searching templates | 60%+ | Keyword mention count |
| JTBD #1 mention rate | 80%+ | "Discover" theme count |
| JTBD #2 mention rate | 50%+ | "Share" theme count |
| JTBD #3 mention rate | 70%+ | "Validate quality" theme count |

---

## Question 2: Willingness-to-Pay Validation

**Research Question**: Is there genuine willingness-to-pay for kit marketplace value (quality curation, GitHub integration, version control) vs. free alternatives (Google search, PromptBase, Notion templates)?

### Hypothesis

**H2.1**: Users and creators value community-curated, GitHub-native kits enough to choose agentii-kit over incumbent free alternatives.

**H2.2**: They perceive specific pain points with free alternatives:
- PromptBase: Low quality, no version control, one-off downloads (no updates)
- Notion templates: Static (not AI-ready), no collaboration, no Git workflow
- Google search: Scattered, low signal, no curation, time-consuming

**H2.3**: 50%+ indicate they'd pay $5-20/mo for premium features (private kits, advanced search, creator monetization, team accounts).

### Validation Approach

**Phase**: Phase 1 - Persona & Problem Validation (Weeks 3-6) + Phase 0 Landing Page (Weeks 1-2)

**Method**: Interview probes + landing page waitlist conversion

**Interview Willingness-to-Pay Probes**:
1. Competitive awareness: "Have you tried PromptBase, Notion templates, or Cursor Rules? What did you like/dislike?"
2. Value perception: "If there were a marketplace with curated, GitHub-native kits, would you use it? Why?"
3. Price sensitivity: "If we added premium features [describe: private kits, team accounts], would you pay for them? How much feels reasonable?"
4. Feature prioritization: "Which would you pay for: (a) private kits, (b) advanced search, (c) priority support, (d) creator monetization?"

**Landing Page Validation**:
- Deploy landing page to kits.agentii.ai (Vercel)
- Measure: Visits → Waitlist signups (conversion rate)
- Hypothesis: If 5%+ conversion (100+ signups from 2000 visits), demand signal exists
- Soft promotion: Twitter (#PMLife, #GrowthMarketing), Reddit (r/ProductManagement, r/marketing), 1 LinkedIn post

### Success Threshold

**GO Criteria**:
- **H2.1 Validated**: 80%+ mention specific incumbent pain points (quote examples for each: PromptBase low quality, Notion static, Google scattered)
- **H2.2 Validated**: 70%+ say they'd choose agentii-kit over free alternatives (because of curation, GitHub, version control)
- **H2.3 Validated**: 50%+ indicate they'd pay $5-20/mo for premium features
- **Landing page**: 5%+ conversion rate (100+ waitlist signups from organic/paid traffic)

**NO-GO Criteria**:
- No differentiation perceived: < 50% see value beyond free alternatives
- Price sensitivity: < 30% willing to pay anything
- Landing page: < 2% conversion (weak demand signal)

**Metrics Collected**:
| Metric | Target | Measurement |
|--------|--------|-------------|
| % mentioning incumbent pain | 80%+ | Theme count (PromptBase, Notion, Google) |
| % preferring agentii-kit | 70%+ | "Would choose this over X" count |
| % willing to pay $5-20/mo | 50%+ | Price probe positive responses |
| Landing page conversion | 5%+ | Waitlist signups / visits |
| Premium feature preference | N/A (explore) | Count by feature (private, search, support, creator $) |

---

## Question 3: User Workflow Validation

**Research Question**: Can Kit Users (non-technical PMs/marketers) realistically complete the "Discover and Fork a Kit" hero workflow in < 10 minutes with acceptable satisfaction?

### Hypothesis

**H3.1**: With GitHub OAuth + one-click fork + video walkthrough, non-technical users can successfully complete the workflow (browse → filter → select → fork → initialize).

**H3.2**: TTFW (Time-to-First-Workflow) target of < 10 minutes is achievable for 70%+ of non-technical users.

**H3.3**: Satisfaction >= 4/5 stars post-workflow (users feel GitHub was "easier than expected").

### Validation Approach

**Phase**: Phase 2 - Hero Workflow Validation (Weeks 7-10)

**Method**: Moderated usability testing with N=10 PM/marketer participants (non-engineers)

**Usability Test Protocol**:
1. **Scenario**: "You need to write a marketing campaign brief for a product launch. Find a kit that helps."
2. **Tasks**:
   - Browse homepage gallery (observe: Do they understand kit categories?)
   - Filter by domain (Marketing) or search ("campaign brief")
   - Click into "Marketing Campaign Kit" card (observe: Do they read details? Check stars/forks?)
   - Click "Fork to GitHub" (observe: GitHub OAuth flow - do they get stuck?)
   - View "Quick Start" guide (observe: Do they understand how to initialize locally?)
3. **Think-aloud protocol**: Narrate what they're doing, what's confusing, what's easy
4. **Measures**:
   - TTFW: Start timer at homepage land, stop at successful fork + Quick Start read
   - Completion: Did they successfully fork? (binary yes/no)
   - Friction points: Where did they hesitate? (tag: GitHub account signup, unclear copy, missing feature)
   - Satisfaction: Post-session 1-5 star rating + open-ended "What was most confusing?"

**Evidence Collection**:
- Screen recording + transcript of think-aloud narration
- TTFW distribution: Min, median, max, % under 10 min
- Friction point tags: GitHub barrier (count), unclear instructions (count), other (specify)
- Quotes: Positive ("Wow, easier than expected") and Negative ("I got stuck at [step]")

### Success Threshold

**GO Criteria**:
- **H3.1 Validated**: 75%+ of users successfully complete workflow (fork kit + understand Quick Start)
- **H3.2 Validated**: 70%+ complete workflow in < 10 min
- **H3.3 Validated**: Satisfaction >= 4.0 average (1-5 scale)

**NO-GO Criteria**:
- Completion < 50%: Workflow too complex; GitHub barrier insurmountable
- TTFW: < 40% complete in < 10 min (target not achievable)
- Satisfaction < 3.5: Users frustrated, not "wow" moment

**Pivot Criteria**:
- GitHub barrier: If < 60% can complete fork, test "Kit Runner" web UI alternative (no GitHub required)
- Persona mismatch: Workflow works for Eng Managers (80% completion) but not Marketers (50%) → shift to technical users first

**Metrics Collected**:
| Metric | Target | Measurement |
|--------|--------|-------------|
| Task completion rate | 75%+ | # successful forks / total tests |
| TTFW < 10 min | 70%+ | # under 10 min / total tests |
| Satisfaction (1-5 scale) | >= 4.0 | Avg post-session rating |
| GitHub barrier friction | < 30% | % who got stuck at GitHub OAuth |
| Quick Start clarity | 80%+ | % who understood next steps |

---

## Question 4: Creator Workflow Validation

**Research Question**: Can Kit Creators complete the "Submit and Share a Kit" workflow in < 5 minutes, and does manual curation (24-48 hour turnaround) meet acceptable quality standards without killing creator motivation?

### Hypothesis

**H4.1**: Kit submission workflow (GitHub OAuth → select repo → fill metadata → submit) can be completed in < 5 minutes by 80%+ of creators.

**H4.2**: Manual curation with 24-48 hour turnaround is acceptable; creators rate feedback 4+ stars even if rejected.

**H4.3**: Abandonment rate after rejection is < 10% (creators iterate and resubmit).

### Validation Approach

**Phase**: Phase 2 - Hero Workflow Validation (Weeks 7-10)

**Method**: Moderated usability testing with N=8 PM/marketer creators (who have created templates before)

**Usability Test Protocol**:
1. **Scenario**: "You've created a PM PRD template you want to share. Submit it to agentii-kit."
2. **Tasks**:
   - Navigate to "Submit a Kit" page
   - GitHub OAuth (if not already authenticated)
   - Select GitHub repo containing kit (observe: Do they understand `.specify/` requirement?)
   - Fill metadata form: Kit name, description, category, tags, example use case
   - Preview kit card (how it will appear in gallery)
   - Submit for review
3. **Simulate manual review**:
   - Show example rejection feedback: "Missing example use case - please add one and resubmit"
   - Show example acceptance notification: "Your kit is live! Here's your dashboard."
4. **Measures**:
   - Time to submission: Start timer at "Submit a Kit" click, stop at submission confirmation
   - Completion: Did they submit successfully? (binary yes/no)
   - Metadata quality: Was form filled correctly? (all required fields, clear description)
   - Curation feedback satisfaction: Post-rejection 1-5 star rating + "Was feedback helpful?"
   - Abandonment intent: "If rejected, would you fix and resubmit or give up?"

**Evidence Collection**:
- Screen recording + time logs
- Submission time distribution: Min, median, max, % under 5 min
- Metadata completeness: % with all required fields filled correctly
- Curation feedback satisfaction: Avg rating (1-5) + quotes
- Abandonment intent: % saying "I'd give up" vs "I'd fix and resubmit"

### Success Threshold

**GO Criteria**:
- **H4.1 Validated**: 80%+ complete submission in < 5 min
- **H4.2 Validated**: 70%+ rate curation feedback 4+ stars (even if rejected)
- **H4.3 Validated**: < 10% indicate they'd abandon after rejection

**NO-GO Criteria**:
- Submission completion < 60%: Workflow too complex; metadata form unclear
- Curation satisfaction < 3.5 stars: Feedback perceived as unhelpful or demotivating
- Abandonment > 30%: Manual curation kills creator motivation

**Pivot Criteria**:
- Submission time: If 50%+ take > 5 min, simplify metadata form (fewer required fields)
- Curation feedback: If < 3.5 stars, provide examples + templates for "good" vs "needs work" kits

**Metrics Collected**:
| Metric | Target | Measurement |
|--------|--------|-------------|
| Submission time < 5 min | 80%+ | # under 5 min / total tests |
| Task completion rate | 80%+ | # successful submissions / total tests |
| Metadata quality | 90%+ | % with all required fields correct |
| Curation feedback rating | >= 4.0 | Avg 1-5 rating (even if rejected) |
| Abandonment intent | < 10% | % saying "I'd give up" |

---

## Question 5: Network Effects Validation

**Research Question**: Does the two-sided marketplace exhibit network effects? Do more kits drive more users, and do more users incentivize more creators?

### Hypothesis

**H5.1**: Each new kit submission drives 5+ new users within 7 days (via social sharing, SEO, creator promotion).

**H5.2**: User-to-creator cross-side conversion is 10%+ (10% of users submit a kit within 30 days).

**H5.3**: Kit count and user signups exhibit strong positive correlation (R² > 0.6).

### Validation Approach

**Phase**: Phase 3 - MVP Beta & Channel Validation (Weeks 11-16)

**Method**: Behavioral analytics during beta launch with 10-15 seed kits + founding creators

**Analytics Instrumentation**:
- Track: Kit submission events (timestamp, creator ID, kit name, social shares)
- Track: User signup events (timestamp, user ID, UTM source, referred by kit link?)
- Track: Cross-side conversion events (user ID → creator ID, first kit submission date)
- Tools: Vercel Analytics (signups), GitHub API (forks/stars), custom events (kit submissions, social shares)

**Measurement Protocol**:
1. **Kit → User correlation**:
   - For each kit submission, measure user signups in 7-day window (before/after)
   - Plot scatter: Kit submission event → Δ user signups
   - Calculate R² and slope (does 1 kit = 5+ users?)
2. **Cross-side conversion**:
   - Cohort: All users who fork a kit (N=100+)
   - Track: % who submit a kit within 30 days
   - Target: 10%+ conversion
3. **Social sharing**:
   - Track: Kit creators sharing their submissions on Twitter/LinkedIn (count links, impressions)
   - Measure: Click-through rate from social → agentii-kit

### Success Threshold

**GO Criteria**:
- **H5.1 Validated**: Each kit drives 5+ new users (on average) within 7 days
- **H5.2 Validated**: Cross-side conversion 10%+ (10+ users out of 100 become creators within 30 days)
- **H5.3 Validated**: R² > 0.6 for kit count → user signup correlation (strong positive relationship)

**NO-GO Criteria**:
- Kit → user correlation weak: < 3 users per kit (network effects absent)
- Cross-side conversion < 5%: Users not becoming creators (one-sided marketplace)
- R² < 0.4: No correlation (kits don't drive users; other factors dominate)

**Pivot Criteria**:
- If network effects weak: Explore alternative models
  - Option A: SaaS tool (B2C subscription, not marketplace) - we curate, users consume
  - Option B: Content site (affiliate/ads) - monetize via traffic, not transactions
- If cross-side conversion low but user engagement high: Focus on user-side first, recruit creators separately

**Metrics Collected**:
| Metric | Target | Measurement |
|--------|--------|-------------|
| Users per kit (7-day window) | 5+ | Δ signups / kit submission |
| Cross-side conversion | 10%+ | # users → creators / total users |
| R² (kit count → signups) | > 0.6 | Correlation analysis |
| Social share rate | 30%+ | % creators sharing on Twitter/LinkedIn |
| Click-through from social | 5%+ | Clicks / impressions |

---

## Question 6: Channel Validation

**Research Question**: Which distribution channel (Product Hunt, Twitter, Reddit, Content) delivers the highest-quality users (activated, retained, referring)?

### Hypothesis

**H6.1**: Product Hunt drives highest volume (500+ visits) but Reddit/communities drive highest quality (D7 retention 40%+ vs PH 25%).

**H6.2**: Twitter drives best balance of activation (20%+) and retention (35%+).

**H6.3**: Clear winner channel exists (2x better combined metric: activation × retention).

### Validation Approach

**Phase**: Phase 3 - MVP Beta & Channel Validation (Weeks 11-16)

**Method**: Multi-channel beta launch with UTM tracking + cohort analysis

**Launch Sequence**:
- **Week 13 Day 1**: Product Hunt launch (primary channel)
- **Week 13 Day 3**: Twitter thread series (secondary channel)
- **Week 13 Day 5**: Reddit posts (r/ProductManagement, r/marketing) (secondary channel)
- **Week 14-16**: Content marketing (publish 2-3 SEO-optimized guides) (tertiary channel)

**Measurement Protocol**:
For EACH channel, track:
1. **Top of funnel**: Visits (UTM-tagged), bounce rate
2. **Activation**: % who fork a kit within first session
3. **Engagement**: % who fork 2+ kits within 7 days
4. **Retention**: Day-7 and Day-30 return visitor rate
5. **Referral**: % who invite a colleague (tracked via referral links)

**Cohort Analysis**:
- Segment users by acquisition source (PH, Twitter, Reddit, Content)
- Compare: Activation, D7 retention, D30 retention, referral rate
- Calculate combined score: Activation × D7 retention (e.g., 20% × 35% = 7.0)
- Winner: Channel with 2x better score than second place

### Success Threshold

**GO Criteria**:
- **H6.1 Validated**: At least 1 channel has activation 15%+ AND D7 retention 30%+
- **H6.2 Validated**: Clear winner identified (combined score 2x+ better than second place)
- **H6.3 Validated**: Winner channel is repeatable (not a one-time spike; consistent over 2+ weeks)

**NO-GO Criteria**:
- All channels < 10% activation: Value prop or hero workflow is broken
- All channels < 20% D7 retention: No stickiness; users try once and don't return
- No clear winner: All channels similar (no differentiation)

**Pivot Criteria**:
- If all channels fail: Revisit JTBD validation from Phase 1 (possible false positive)
- If paid channels work but organic doesn't: Consider direct sales (outbound) instead of PLG
- If only one persona segment activates: Narrow focus to that segment (e.g., Eng Managers only)

**Metrics Collected**:
| Channel | Visits | Activation | D7 Retention | Combined Score | Winner? |
|---------|--------|-----------|-------------|----------------|---------|
| Product Hunt | [measure] | [%] | [%] | [A × D7] | TBD |
| Twitter | [measure] | [%] | [%] | [A × D7] | TBD |
| Reddit | [measure] | [%] | [%] | [A × D7] | TBD |
| Content SEO | [measure] | [%] | [%] | [A × D7] | TBD |

**Success Threshold**: Winner channel has combined score 2x+ better than second place

---

## Summary: Research Question Alignment

| Question | Phase | Method | Success Metric | Traceable to Spec |
|----------|-------|--------|----------------|-------------------|
| Q1: Persona & JTBD | Phase 1 | Interviews (N=20) | 70%+ report 2+ hrs/week pain | spec.md lines 72-118 (JTBD) |
| Q2: Willingness-to-Pay | Phase 1 + Landing Page | Interview probes + conversion | 50%+ willing to pay; 5%+ landing page conversion | spec.md lines 327-331 (Open Question 3) |
| Q3: User Workflow | Phase 2 | Usability tests (N=10) | 75%+ completion; TTFW < 10 min | spec.md lines 124-150 (Hero Workflow 1) |
| Q4: Creator Workflow | Phase 2 | Usability tests (N=8) | 80%+ submission < 5 min; 70%+ curation satisfaction | spec.md lines 152-182 (Hero Workflow 2) |
| Q5: Network Effects | Phase 3 | Behavioral analytics | 5+ users per kit; 10%+ cross-side conversion | spec.md lines 54-72 (Principle I: Two-Sided Marketplace) |
| Q6: Channel | Phase 3 | Multi-channel launch | 15%+ activation; 30%+ D7 retention; clear winner | spec.md lines 275-308 (Distribution Hypotheses) |

All research questions are directly traceable to PMF spec hypotheses and constitution principles. No orphaned research activities.
