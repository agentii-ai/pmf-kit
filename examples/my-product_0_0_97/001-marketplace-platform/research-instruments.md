# Research Instruments: Agentii-Kit Marketplace

**Branch**: `001-marketplace-platform`
**Created**: 2025-12-05
**Status**: Research Planning
**Research Lead**: Product/Research Lead

## Overview

This document contains all research instruments (interview guides, usability test protocols, survey templates, experiment protocols) needed to execute the research questions defined in `research-questions.md`.

---

## Interview Guide #1: Problem & Persona Validation (Phase 1)

**Purpose**: Validate personas have real, frequent pain and actively seek templates/playbooks (RQ1, RQ3, RQ6)

**Target**: Kit Creators (N=10) and Kit Users (N=10)

**Duration**: 45-60 minutes

**Incentive**: $50/participant

### Screener Questions (Email/DM Screening)

1. **Role/Title**: What is your current job title and primary role?
   - Target: Marketing ops, product manager, startup founder, operations lead
   - Disqualify: Individual contributor devs, hobbyists without workflow pain

2. **Workflow Frequency**: How many times in the past 6 months have you created similar projects/campaigns/features (e.g., marketing campaigns, PRDs, launch checklists)?
   - Target: ≥5 times (repeated workflow pain)
   - Disqualify: <3 times (insufficient repetition)

3. **Tools Used**: What tools do you currently use for project/campaign planning?
   - Target: Notion, Asana, Google Docs, spreadsheets (manual workarounds)
   - Bonus: GitHub, AI agents (tech-savvy)

4. **Template Seeking Behavior**: Have you ever searched for or purchased templates/playbooks for your work (e.g., Notion templates, courses, blog posts)?
   - Target: Yes (willingness-to-try signal)
   - Accept: No, but interested (potential early adopter)

### Interview Protocol

**Part 1: Context Setting (5 min)**

- **Intro**: "Thank you for joining! We're researching how professionals organize and execute recurring workflows. This is not a sales call—we want to understand your pain points and current solutions. There are no right or wrong answers."
- **Recording consent**: "May I record this session for note-taking? Your responses will be anonymized."
- **Icebreaker**: "Tell me about your role and a typical project you work on frequently."

**Part 2: Pain Discovery (20 min)**

- **Current workflow**:
  - "Walk me through the last time you started [campaign/PRD/project]. What were the first 3 things you did?"
  - "How long did it take to set up the project structure (docs, tasks, templates) before actual execution?"
  - Probe: "Was that typical, or was this project unusual?"

- **Pain frequency**:
  - "How often do you start projects like this? (weekly, monthly, quarterly)"
  - "How much time do you spend on setup vs. execution?"
  - Probe: "If you could save 2 hours per project setup, what would that enable you to do?"

- **Current workarounds**:
  - "Do you have a standard process or template you use?"
  - "Where do you get templates/structure? (copy-paste from old projects, Google, Notion marketplace, colleagues)"
  - Probe: "Have you ever purchased a template or course? How much did you pay?"

- **Emotional impact**:
  - "How do you feel when you start a new project from a blank page?"
  - Listen for: frustration, wasted time, feeling scattered, forgetting important steps
  - Probe: "Has lack of structure ever caused rework or mistakes?"

**Part 3: Willingness-to-Pay & Alternatives (15 min)**

- **Current spend**:
  - "Have you spent money on tools to solve this problem? (Notion templates, courses, consultants)"
  - "How much have you spent in the past year?"
  - Probe: "What did you get for that money? Was it worth it?"

- **Hypothetical solution**:
  - "Imagine a marketplace of structured workflow templates for your job (marketing, PM, legal, etc.)—all open-source and forkable on GitHub. Would that be useful?"
  - "What would make you use it? What would make you avoid it?"
  - Probe: "Would you pay for premium features like analytics or private templates? How much?"

- **Competitive alternatives**:
  - "What other solutions have you tried? (Notion, Asana templates, blog posts, courses)"
  - "Why did you stop using them or why aren't they sufficient?"

**Part 4: Creator Motivation (10 min) - *For Kit Creator personas only***

- **Sharing motivation**:
  - "Have you ever documented your workflow to share with colleagues or the public?"
  - "What motivated you to do that? (reduce duplicate questions, build reputation, intrinsic satisfaction)"
  - Probe: "How long did it take to document? Would you do it again?"

- **Friction**:
  - "What prevents you from documenting your workflows more often?"
  - Listen for: time investment, unclear structure, no perceived benefit
  - Probe: "If you could publish a template in <5 minutes, would you?"

- **Incentives**:
  - "Would you be motivated by reputation scores, usage stats, or community recognition?"
  - "What would make you want to maintain your templates over time?"

**Part 5: Wrap-Up (5 min)**

- **Open feedback**: "Is there anything we didn't cover that's important for you?"
- **Early access offer**: "We're building this marketplace and looking for early users/creators. Would you be interested in early access?"
- **Thank you + incentive delivery**

### Data to Collect

- [ ] Frequency of pain (hours/week wasted on setup)
- [ ] Current workarounds (tools, templates, processes)
- [ ] Willingness-to-pay signals (money spent, hypothetical WTP)
- [ ] Verbatim quotes (for persona pain profiles)
- [ ] Creator motivations and friction points
- [ ] Early access interest (Y/N)

---

## Usability Test Protocol #1: Hero Workflow Validation (Phase 2)

**Purpose**: Validate Hero Workflow 1 (Discover and Fork a Kit) can be completed in <10 minutes by non-developers (RQ2, RQ5, RQ7)

**Target**: Non-developer Kit Users (N=5: marketers, PMs, founders)

**Duration**: 45-60 minutes (includes setup, test, debrief)

**Incentive**: $50/participant

### Test Setup

**Prerequisites**:
- Mockup/prototype of marketplace homepage (Figma or live staging site)
- 5-10 sample kits (marketing, PM, legal, startup categories)
- Test user has GitHub account (confirm during screening)
- Screen recording software (Zoom, Loom, or similar)

**Test Environment**:
- User's own computer (to capture real friction with tools)
- Moderator shares mockup/prototype link
- User shares screen during test

### Test Protocol

**Part 1: Context Setting (5 min)**

- **Intro**: "Today we're testing a new marketplace for workflow templates. Your honest feedback will help us improve. There are no wrong answers—if you get stuck, that's valuable feedback."
- **Scenario**: "Imagine you need to [launch a marketing campaign / write a PRD / create Terms of Service]. You've heard about a marketplace where you can find structured templates. Your goal is to find a template, fork it, and start your first task."
- **Think-aloud**: "Please narrate your thought process as you go. Tell me what you're looking for, what you're confused about, and what you expect to happen."

**Part 2: Hero Workflow Test (Target: <10 min)**

**Task 1: Discover a Kit** (Target: <3 min)

- **Instruction**: "Go to the marketplace homepage [share link]. Find a template for [your scenario]."
- **Observations**:
  - Does user use search, browse categories, or curated collections?
  - How long does it take to find a relevant kit?
  - Does user understand kit card information (description, stars, compatibility badges)?
- **Friction points**: Document where user hesitates, clicks back, or expresses confusion

**Task 2: Fork the Kit** (Target: <2 min)

- **Instruction**: "You've found the [kit name]. Fork it to your GitHub account."
- **Observations**:
  - Does user understand "Fork to GitHub" button?
  - Does GitHub fork workflow succeed without errors?
  - Does user understand what happens after fork (receives confirmation, repo URL)?
- **Friction points**: GitHub auth issues, fork fails, user confused about what "fork" means

**Task 3: Customize and Execute** (Target: <5 min)

- **Instruction**: "Open your forked repo. Customize the template for your scenario and start your first task."
- **Observations**:
  - Does user understand the 4-file structure (constitution, spec, plan, tasks)?
  - Does user successfully customize `constitution.md` or `spec-template.md`?
  - Does user attempt to use AI agent (Claude Code, Cursor) or manual editing?
  - Does user complete first task (e.g., fill out first section of spec)?
- **Friction points**: Doesn't understand where to start, confused by template placeholders, AI agent not installed

**Part 3: Post-Task Debrief (10 min)**

- **Satisfaction**: "On a scale of 1-5, how satisfied are you with that experience? Why?"
- **Wow moment**: "Did you have an 'aha' moment where you felt value? When?"
- **Friction**: "What was the hardest part? Where did you get stuck?"
- **Comparison**: "How does this compare to your current workflow (Google search, copy-paste from old projects)?"
- **Willingness to return**: "Would you use this again? Would you recommend it to a colleague?"

**Part 4: Discovery UX Test (A/B Variant) (10 min)**

- **Variant A (Curated Collections)**: Show homepage with "Editor's Choice", "Trending", "Most Forked" sections
- **Variant B (Open Browse)**: Show homepage with search bar + category filters (Marketing, Product, Legal, etc.)

**Question**: "Which of these two layouts would you prefer for discovering kits? Why?"

- Listen for: "Curated saves time" vs. "Search gives control"
- Measure: Preference (A vs. B), time-to-kit-selection, perceived value

**Part 5: Trust Signals Test (Reputation Scoring) (5 min)**

- **Show two kit cards**:
  - Kit A: "Marketing Campaign Kit" | 150 stars | 45 forks | Last updated 2 weeks ago | **Creator: Expert (300 reputation)**
  - Kit B: "Marketing Campaign Kit" | 200 stars | 60 forks | Last updated 1 week ago | **Creator: Newcomer (10 reputation)**

**Question**: "Which kit would you choose? Why?"

- Listen for: Do users care about creator reputation, or just stars/forks/recency?
- Measure: Selection (A vs. B), rationale

### Data to Collect

- [ ] Time-to-first-task (from landing to executing first task)
- [ ] Friction points (where user got stuck, duration of confusion)
- [ ] Satisfaction rating (1-5 scale)
- [ ] Wow moment observed (Y/N, timestamp, verbatim quote)
- [ ] Discovery preference (curated vs. browse)
- [ ] Trust signal preference (reputation vs. stars/forks)

---

## Multi-Agent Compatibility Test #1: Technical Validation (Phase 1)

**Purpose**: Validate kits work across ≥2 AI agents with ≥80% compatibility (RQ4)

**Target**: 10 seed kits (diverse domains: marketing, PM, legal, startup, education)

**Duration**: 2-3 weeks

**Team**: Engineering Lead + 1-2 testers

### Test Setup

**Prerequisites**:
- Install Claude Code, Cursor, and GitHub Copilot on test machines
- Prepare 10 seed kits (ensure all have 4-file structure, README, examples)
- Create compatibility tracking spreadsheet (kit × agent → pass/fail/workaround)

### Test Protocol

**For Each Kit**:

**Step 1: Test with Claude Code** (Primary Agent)

1. Fork kit to test GitHub account
2. Open kit in Claude Code environment
3. Run hero workflow: `/agentiikits.specify [example scenario from README]`
4. Execute generated spec/plan/tasks using `/agentiikits.plan` and `/agentiikits.tasks`
5. **Record**:
   - Success (Y/N): Did workflow complete without errors?
   - Errors encountered (command syntax, file access, missing dependencies)
   - Workarounds needed (manual fixes, file edits)
   - Time to complete (minutes)

**Step 2: Test with Cursor** (Secondary Agent)

1. Fork same kit to test GitHub account
2. Open kit in Cursor environment
3. Run equivalent workflow (adjust command syntax if needed based on Cursor docs)
4. Execute generated spec/plan/tasks
5. **Record**: Same metrics as Step 1

**Step 3: Test with GitHub Copilot** (Tertiary Agent)

1. Fork same kit to test GitHub account
2. Open kit in VS Code + Copilot
3. Run equivalent workflow (if Copilot supports custom commands; otherwise manual execution)
4. Execute generated spec/plan/tasks
5. **Record**: Same metrics as Step 1

**Step 4: Document Compatibility**

- **Pass**: Kit works without modification across agent
- **Workaround**: Kit requires documented fix (e.g., adjust command syntax in README)
- **Fail**: Kit cannot work with agent (fundamental incompatibility)

### Compatibility Matrix

| Kit Name | Domain | Claude Code | Cursor | Copilot | Compatible Agents | Notes |
|----------|--------|-------------|--------|---------|-------------------|-------|
| Marketing Campaign Kit | Marketing | Pass | Pass (workaround: adjust slash commands) | Fail (no custom commands) | 2/3 | Document Cursor workaround in README |
| PM PRD Kit | Product | Pass | Pass | Pass | 3/3 | Fully compatible |
| ... | ... | ... | ... | ... | ... | ... |

### Success Criteria

- [ ] ≥80% of kits work with Claude Code + Cursor (≥8/10 kits)
- [ ] ≥60% of kits work with all 3 agents (≥6/10 kits)
- [ ] All incompatibilities have documented workarounds (<5 min to apply)
- [ ] Update constitution if ≥80% threshold not met (adjust expectations or fix kits)

### Data to Collect

- [ ] Compatibility matrix (10 kits × 3 agents = 30 test runs)
- [ ] Agent-specific failure modes (command syntax, file access, etc.)
- [ ] Workaround documentation (steps to fix, time to apply)
- [ ] Recommendations for kit README templates (e.g., "Tested with Claude Code, Cursor; Copilot requires manual execution")

---

## Survey Template #1: Willingness-to-Pay (Phase 1 & 3)

**Purpose**: Quantify willingness-to-pay for premium features (analytics, private kits)

**Target**: Interview participants (N=20) and beta users (N=50+)

**Distribution**: Email after interview or in-app survey after 7 days of usage

### Survey Questions

**Q1: How much time did you save using agentii-kit compared to your previous workflow?**

- [ ] <1 hour
- [ ] 1-2 hours
- [ ] 2-4 hours
- [ ] 4+ hours
- [ ] I didn't save time

**Q2: How likely are you to use agentii-kit again? (1-5 scale)**

- 1 (Very unlikely) → 5 (Very likely)

**Q3: Would you recommend agentii-kit to a colleague? (NPS)**

- 0 (Not at all likely) → 10 (Extremely likely)

**Q4: Which premium features would you pay for? (Select all that apply)**

- [ ] Kit usage analytics (forks, stars, user feedback)
- [ ] Private kits (for team/organization only)
- [ ] Premium support (priority bug fixes, 1-on-1 help)
- [ ] Advanced search/filters (by industry, use case, complexity)
- [ ] Kit versioning UI (compare versions, rollback)
- [ ] API access (programmatic kit submission/retrieval)
- [ ] None, I prefer free/open-source only

**Q5: How much would you pay per month for those premium features?**

- [ ] $0 (I would not pay)
- [ ] $5-10/month
- [ ] $10-20/month
- [ ] $20-50/month
- [ ] $50+/month

**Q6: What would make you stop using agentii-kit? (Open-ended)**

---

## Experiment Protocol #1: Multi-Channel Launch (Phase 3)

**Purpose**: Identify distribution channels with highest activation and retention (RQ9)

**Target**: Launch across 4 channels, track N=50+ signups per channel

**Duration**: 6-8 weeks

### Channel Definitions

**Channel 1: Product Hunt**

- **Timing**: Week 1 (launch day)
- **Content**: Product Hunt listing with screenshots, demo video, value prop
- **Goal**: 100+ high-quality signups (users who fork ≥1 kit) in first week
- **UTM**: `?utm_source=producthunt&utm_medium=launch&utm_campaign=001-marketplace-platform`

**Channel 2: Twitter/X**

- **Timing**: Weeks 1-2
- **Content**: Problem-solution threads, real examples ("I saved 10 hours this week"), demo videos
- **Goal**: 50+ signups from Twitter in 2 weeks
- **UTM**: `?utm_source=twitter&utm_medium=social&utm_campaign=001-marketplace-platform`

**Channel 3: Reddit Communities**

- **Timing**: Weeks 2-3
- **Subreddits**: r/ProductManagement, r/marketing, r/SideProject, r/MachineLearning
- **Content**: "I made this" posts with genuine value (not spammy)
- **Goal**: 30+ signups from Reddit in 2 weeks
- **UTM**: `?utm_source=reddit&utm_medium=community&utm_campaign=001-marketplace-platform`

**Channel 4: GitHub Trending**

- **Timing**: Weeks 1-4
- **Content**: Seed 10 kits as standalone GitHub repos with links back to marketplace
- **Goal**: 1-2 kits trend on GitHub, drive 50+ signups
- **UTM**: `?utm_source=github&utm_medium=organic&utm_campaign=001-marketplace-platform`

### Instrumentation

**Metrics to Track (by UTM source)**:

- **Signups**: Total users who land on marketplace (tracked via Vercel Analytics + UTM)
- **Activation**: % who fork ≥1 kit within first session
- **D7 Retention**: % who return and fork another kit within 7 days
- **D30 Retention**: % who remain active after 30 days
- **Cost-per-activation**: Time/money invested per channel ÷ activated users

### Analysis

**Week 4 Review**:
- Rank channels by activation rate
- Rank channels by D7 retention
- Calculate cost-per-activation by channel
- **Decision**: Double down on top 2 channels, reduce investment in low-performing channels

**Week 8 Review**:
- Measure D30 retention by channel
- Identify high-quality vs. high-volume channels
- **Decision**: Post-launch channel strategy (focus on quality or volume)

---

## Next Steps

1. **Recruit participants**: Screen and schedule 20 interviews (Phase 1) + 10 usability tests (Phase 2)
2. **Prepare test assets**: Marketplace mockups, sample kits, GitHub repos for testing
3. **Instrument metrics**: Set up Vercel Analytics, GitHub API sync, UTM tracking
4. **Generate validation checkpoints**: Define go/kill/pivot criteria for each PDCA gate (see `validation-checkpoints.md`)
