# Validation Checkpoints: Agentii-Kit Marketplace

**Branch**: `001-marketplace-platform`
**Created**: 2025-12-05
**Status**: Research Planning
**Research Lead**: Product/Research Lead

## Overview

This document defines go/kill/pivot criteria for each PDCA (Plan-Do-Check-Act) decision gate in the research plan. Each checkpoint specifies what we measure, when we measure it, who decides, and what actions to take based on results.

---

## Phase 1 → Phase 2 Gate: Persona & Problem Validation

**Timeline**: End of Week 4 (Phase 1)

**Decision Authority**: Product Lead + Research Lead

### Checkpoint 1.1: Persona Pain Validation (RQ1)

**What we measure**:
- % of interviewed personas (N=20) who report workflow setup pain ≥2 hours/week
- % who mention actively searching for templates/playbooks
- Quality of verbatim quotes (pain is frequent, substantial, and urgent)

**Success Thresholds**:
- **GO**: ≥70% report pain ≥2 hours/week AND ≥50% actively search for templates
- **PIVOT**: 50-69% report pain → Focus on highest-pain persona only (e.g., Kit Creators over Kit Users)
- **KILL**: <50% report pain → Insufficient market need, abandon marketplace

**Data Source**: Interview synthesis from `research-instruments.md` → Interview Guide #1

**Review Date**: End of Week 4

**Actions**:
- **GO**: Advance to Phase 2 (usability testing)
- **PIVOT**: Re-target spec to focus on highest-pain persona; re-interview 5-10 additional personas
- **KILL**: Document learnings; consider alternative product directions

---

### Checkpoint 1.2: Creator Recruitment Feasibility (RQ6)

**What we measure**:
- Number of creators recruited (target: ≥10 commits)
- Creator outreach response rate (target: ≥30% reply to DM)
- Creator acceptance rate (target: ≥50% commit to publishing)

**Success Thresholds**:
- **GO**: ≥10 creators committed to publishing within 4 weeks
- **PIVOT**: 5-9 creators → Offer stronger incentives (early access, featured placement, analytics preview) OR extend recruitment timeline
- **KILL**: <5 creators → Supply-side failure, marketplace not viable without creator seeding

**Data Source**: Creator outreach tracking spreadsheet + interview notes

**Review Date**: End of Week 3 (earlier gate to allow pivot time)

**Actions**:
- **GO**: Proceed with Phase 2; creators in pipeline to publish during Phase 3 beta
- **PIVOT**: Increase incentives; recruit from different channels (Twitter DMs, LinkedIn, Discord)
- **KILL**: Pivot to different model (e.g., team-created kits only, no community contribution)

---

### Checkpoint 1.3: Cross-Agent Compatibility Feasibility (RQ4)

**What we measure**:
- % of tested kits (N=10) that work with Claude Code + Cursor without modification
- % of tested kits that work with all 3 agents (Claude, Cursor, Copilot)
- Severity of agent-specific issues (can workarounds be documented in <5 min?)

**Success Thresholds**:
- **GO**: ≥80% work with Claude Code + Cursor (≥8/10 kits)
- **PIVOT**: 60-79% work → Document workarounds aggressively; update kit READMEs; adjust constitution threshold to 70%
- **KILL**: <60% work → Multi-agent compatibility not achievable; pivot to single-agent focus (Claude Code only)

**Data Source**: Compatibility matrix from `research-instruments.md` → Multi-Agent Compatibility Test #1

**Review Date**: End of Week 3

**Actions**:
- **GO**: Maintain ≥80% compatibility threshold in constitution; display compatibility badges in marketplace
- **PIVOT**: Lower threshold; invest in workaround documentation; provide agent-specific setup guides
- **KILL**: Update constitution to remove multi-agent requirement; focus MVP on Claude Code only

---

### Checkpoint 1.4: Willingness-to-Pay Signals (RQ3)

**What we measure**:
- % of interviewed personas who indicate willingness-to-pay for premium features
- Price points mentioned ($5-10, $10-20, $20-50/month)
- Evidence of past spend on templates/courses (actual money spent, not hypothetical)

**Success Thresholds**:
- **GO**: ≥40% indicate WTP for premium features AND past spend evidence exists ($10-500/year on templates/courses)
- **PIVOT**: 20-39% indicate WTP → Monetization viable but not immediate; focus on free MVP, defer premium features
- **NO ACTION REQUIRED**: <20% indicate WTP → Expected for MVP; proceed with free tier only

**Data Source**: Interview responses to willingness-to-pay probes + survey data

**Review Date**: End of Week 4

**Actions**:
- **GO**: Plan post-MVP monetization roadmap (analytics, private kits)
- **PIVOT**: Focus on proving free tier value first; revisit monetization post-PMF
- **NO ACTION**: Free tier only for MVP; monetization deferred to post-PMF

---

## Phase 2 → Phase 3 Gate: Hero Workflow & UX Validation

**Timeline**: End of Week 7 (Phase 2)

**Decision Authority**: Product Lead + UX/Design Lead

### Checkpoint 2.1: Hero Workflow 1 TTFW (RQ2)

**What we measure**:
- % of non-developer users (N=10) who complete Hero Workflow 1 in ≤10 minutes
- Satisfaction ratings (1-5 scale, target ≥4/5)
- Observation of "wow moment" (target ≥60% of sessions)

**Success Thresholds**:
- **GO**: ≥75% complete in ≤10 min AND ≥70% rate ≥4/5 stars AND ≥60% have "wow moment"
- **PIVOT**: 50-74% complete in ≤10 min → Redesign UX friction points (GitHub fork flow, template customization instructions, AI agent onboarding)
- **KILL**: <50% complete in ≤10 min → TTFW unachievable for non-developers; pivot to developer-only audience

**Data Source**: Usability test recordings + post-task debrief notes from `research-instruments.md` → Usability Test Protocol #1

**Review Date**: End of Week 7

**Actions**:
- **GO**: Launch Phase 3 beta with current UX
- **PIVOT**: Redesign friction points (add tutorial video, simplify "fork" language, provide example customizations); re-test with 5 additional users
- **KILL**: Update personas to focus on developers only (abandon non-developer market); adjust positioning

---

### Checkpoint 2.2: Persona Retention Ranking (RQ3)

**What we measure**:
- Estimated D7/D30 retention by persona (from interview willingness-to-return + Phase 1 follow-up)
- Persona-specific engagement patterns (repeat usage likelihood)

**Success Thresholds**:
- **GO**: Clear ranking established (e.g., "Kit Users > Startup Founders > Kit Creators") with ≥1 persona showing D7 potential ≥30%
- **PIVOT**: No clear ranking → Focus MVP on all personas equally; measure retention in Phase 3 beta
- **NO ACTION REQUIRED**: All personas show similar retention potential

**Data Source**: Interview responses ("Would you use this weekly?" "Would you recommend it?") + survey data

**Review Date**: End of Week 7

**Actions**:
- **GO**: Prioritize highest-retention persona in Phase 3 onboarding and messaging
- **PIVOT**: Launch beta with equal persona focus; measure actual retention to inform post-MVP prioritization
- **NO ACTION**: Proceed with multi-persona approach

---

### Checkpoint 2.3: Discovery UX Preference (RQ5)

**What we measure**:
- User preference (curated collections vs. open browse/search)
- Time-to-kit-selection by discovery method
- Persona-specific patterns (do non-devs prefer curated? do PMs prefer search?)

**Success Thresholds**:
- **GO**: Clear preference emerges (≥60% prefer curated OR ≥60% prefer browse/search)
- **HYBRID**: 40-60% split → Build both (curated homepage + search/filter available)
- **NO STRONG PREFERENCE**: < 40-60% split is fine → Default to hybrid approach

**Data Source**: Usability test observations + post-task preference questions

**Review Date**: End of Week 7

**Actions**:
- **GO (Curated)**: MVP homepage features "Editor's Choice", "Trending", "Most Forked" sections
- **GO (Browse)**: MVP homepage features search bar + category filters (Marketing, Product, Legal, etc.)
- **HYBRID**: MVP homepage has curated section + search bar (slightly more complex but accommodates both preferences)

---

### Checkpoint 2.4: Creator Reputation Necessity (RQ7)

**What we measure**:
- User reliance on creator reputation scores vs. other trust signals (stars, forks, recency)
- Selection behavior (do users choose high-reputation creators even with lower stars?)

**Success Thresholds**:
- **BUILD IN MVP**: ≥60% of users prefer kits from "Expert" creators (high reputation) even with lower stars/forks
- **DEFER TO POST-PMF**: <40% mention creator reputation as important → Focus on stars/forks/recency only for MVP

**Data Source**: Usability test trust signals experiment

**Review Date**: End of Week 7

**Actions**:
- **BUILD**: Add creator reputation scoring to MVP (Newcomer, Contributor, Expert, Legend tiers)
- **DEFER**: Remove reputation scoring from MVP scope; rely on GitHub stars/forks/recency for trust signals

---

## Phase 3 → Post-PMF Gate: Network Effects & Channel Validation

**Timeline**: End of Week 15 (Phase 3, 6-8 weeks)

**Decision Authority**: Product Lead + Growth Lead

### Checkpoint 3.1: Network Effects Validation (RQ8)

**What we measure**:
- Correlation (R²) between kit count and user signups (time series data, weekly)
- Cross-side conversion rate (% of users who fork ≥1 kit → submit ≥1 kit within 90 days)
- Creator-to-user ratio over time (target 1:10 to 1:20)

**Success Thresholds**:
- **GO**: R² > 0.4 AND cross-side conversion ≥10% AND creator-to-user ratio in range 1:10 to 1:20
- **PIVOT**: R² 0.2-0.4 OR conversion 5-9% → Network effects exist but weak; invest in creator incentives (reputation, analytics, featured placement)
- **KILL**: R² < 0.2 OR conversion <5% → No network effects; pivot to team-curated marketplace (no community contribution)

**Data Source**: Vercel Analytics (user signups) + GitHub API (kit count) + internal database (forks, submissions)

**Review Date**: End of Week 15

**Actions**:
- **GO**: Scale marketplace; invest in growth (more creators, more categories, more channels)
- **PIVOT**: Strengthen creator incentives; gamify submissions; add leaderboards/badges
- **KILL**: Pivot to curated model; team creates all kits; no community marketplace

---

### Checkpoint 3.2: Channel Quality Ranking (RQ9)

**What we measure**:
- Activation rate by channel (% who fork ≥1 kit)
- D7 retention by channel
- D30 retention by channel
- Cost-per-activation by channel (time/money invested)

**Success Thresholds**:
- **GO**: Identify 1-2 channels with activation ≥15% AND D7 retention ≥30%
- **PIVOT**: No channel hits thresholds → Test 2-3 new channels (LinkedIn, Discord, HackerNews, SEO)
- **KILL**: All channels show <10% activation AND <20% D7 retention → Distribution failure; reconsider positioning or target audience

**Data Source**: UTM tracking + cohort analysis from `research-instruments.md` → Experiment Protocol #1

**Review Date**: Week 11 (interim check) + Week 15 (final check)

**Actions**:
- **GO**: Double down on top 2 channels; reduce investment in low-quality channels
- **PIVOT**: Test new channels; adjust messaging/positioning; consider paid acquisition
- **KILL**: Re-evaluate product positioning; consider different target audience or use case

---

### Checkpoint 3.3: Marketplace Metrics (Overall PMF)

**What we measure**:
- D7 retention (target ≥30% for users who fork ≥1 kit)
- D30 retention (target ≥20%)
- Monthly Active Kits (MAK) (target ≥50 kits forked/downloaded per month by month 6)
- NPS from activated users (target ≥50)
- Sean Ellis test (target ≥40% "very disappointed" without product)

**Success Thresholds**:
- **SCALE**: D7 ≥30%, D30 ≥20%, MAK ≥50, NPS ≥50, Sean Ellis ≥40% → PMF achieved, invest in growth
- **ITERATE**: D7 20-29%, D30 10-19%, MAK 30-49, NPS 30-49, Sean Ellis 30-39% → Weak PMF signals; iterate on UX, positioning, or features
- **PIVOT**: D7 <20%, D30 <10%, MAK <30, NPS <30, Sean Ellis <30% → No PMF; major pivot required (audience, use case, or product model)

**Data Source**: Vercel Analytics, GitHub API, NPS survey, Sean Ellis survey (sent to activated users at Day 30)

**Review Date**: End of Week 15 (final gate before scale decision)

**Actions**:
- **SCALE**: Invest in growth (paid acquisition, content marketing, partnerships); expand kit categories; add premium features
- **ITERATE**: Run `/pmfkit.optimize` to refine hypotheses; conduct 5-10 follow-up interviews with churned users; A/B test UX improvements
- **PIVOT**: Return to Phase 1 (re-interview personas); consider alternative audience (enterprise vs. SMB) or use case (team kits vs. individual kits)

---

## PDCA Cycle Summary

| Phase | Duration | Key Checkpoints | Decision Gate | Actions |
|-------|----------|----------------|---------------|---------|
| **Phase 1: Problem & Persona Validation** | 4 weeks | Persona pain (≥70%), Creator recruitment (≥10), Cross-agent compatibility (≥80%), WTP signals (≥40%) | **Phase 1 → 2** | GO: Advance to usability testing / PIVOT: Re-target persona or adjust thresholds / KILL: Abandon marketplace |
| **Phase 2: Hero Workflow Validation** | 3 weeks | TTFW <10 min (≥75%), Persona retention ranking, Discovery UX preference, Creator reputation necessity | **Phase 2 → 3** | GO: Launch beta / PIVOT: Redesign UX friction points / KILL: Pivot to dev-only audience |
| **Phase 3: Network Effects & Channels** | 6-8 weeks | Network effects (R² > 0.4, conversion ≥10%), Channel quality (activation ≥15%, D7 ≥30%), Overall PMF (D7 ≥30%, NPS ≥50) | **Phase 3 → Scale** | SCALE: Invest in growth / ITERATE: Optimize UX/positioning / PIVOT: Major product/audience change |

---

## Review Cadence

- **Weekly PMF Review**: Every Monday, 45 minutes
  - **Agenda**: Metrics review (10 min), learnings (15 min), blockers (10 min), decisions (5 min), next week (5 min)
  - **Attendees**: Product Lead, Research Lead, Eng Lead, Design Lead
  - **Output**: Updated dashboard, task priorities, documented decisions

- **Phase Gate Reviews**: End of Week 4, Week 7, Week 15
  - **Format**: 90-minute deep dive with all checkpoint data
  - **Decision**: GO / PIVOT / KILL with explicit rationale
  - **Output**: Phase gate decision document (linked to this file)

---

## Escalation Protocol

**If checkpoint fails unexpectedly**:
1. Document failure mode (what was expected, what happened, root cause hypothesis)
2. Escalate to Product Lead + Research Lead within 24 hours
3. Convene emergency decision meeting (GO / PIVOT / KILL)
4. Update this document with revised success thresholds or timeline

**If external blocker occurs** (e.g., GitHub API rate limits, beta user recruitment fails):
1. Document blocker and estimated impact (days delayed, sample size reduced)
2. Propose mitigation plan (extend timeline, reduce sample size, use alternative data source)
3. Get approval from Product Lead before proceeding

---

## Next Steps

1. **Instrument Phase 1 metrics**: Set up interview synthesis spreadsheet, creator recruitment tracker, compatibility matrix
2. **Schedule Phase 1 Gate Review**: Book 90-minute meeting for end of Week 4
3. **Prepare Phase 1 → 2 decision document template**: Pre-fill with success thresholds from this file
4. **Begin Phase 1 execution**: Recruit and schedule 20 interviews + 30 creator outreach targets
