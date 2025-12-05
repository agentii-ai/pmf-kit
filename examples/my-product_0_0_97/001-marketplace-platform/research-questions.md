# Research Questions: Agentii-Kit Marketplace

**Branch**: `001-marketplace-platform`
**Created**: 2025-12-05
**Status**: Research Planning
**Research Lead**: Product/Research Lead

## Overview

This document operationalizes all hypotheses from the PMF spec into testable research questions. Each question maps to specific methodologies, sample sizes, success criteria, and validation gates.

---

## Research Question 1 (P1): Do Kit Creator and Kit User personas have real, frequent pain requiring our solution?

**Hypothesis**: Marketing ops leads, PMs, and startup founders waste 2-3 hours per week reinventing workflows that should be standardized, and actively seek templates/playbooks.

**Research Question**: What percentage of target personas (Kit Creators and Kit Users) experience workflow setup pain ≥2 hours/week and actively search for templates/playbooks?

**Methodology**:
- **Phase 1 Interviews** (N=20): 45-60 min problem-focused interviews
  - 10 interviews with Kit Creator personas (marketing ops, senior PMs with repeated workflows)
  - 10 interviews with Kit User personas (PMs, marketers, startup founders)
- **Screening criteria**: Must have created/used ≥5 similar projects in past 6 months
- **Interview protocol**: See `research-instruments.md` → Interview Guide #1

**Success Criteria**:
- **Pass**: ≥70% of interviewed personas report workflow setup pain ≥2 hours/week
- **Pass**: ≥50% mention actively searching for templates/playbooks (Google searches, Notion marketplace, etc.)
- **Pass**: Verbatim quotes confirm pain is frequent and substantial ("every campaign starts from scratch", "I waste hours")

**Evidence to Collect**:
- Frequency of pain (hours/week wasted)
- Current workarounds (copy-paste, Google, Notion templates)
- Willingness-to-pay signals (money spent on templates, courses, consultants)
- Verbatim quotes for pain profile validation

---

## Research Question 2 (P1): Can Hero Workflow 1 (Discover and Fork a Kit) be completed in <10 minutes by non-developers?

**Hypothesis**: Non-developers (marketers, PMs, lawyers) can discover a kit, fork it to GitHub, and start first task within 10 minutes.

**Research Question**: What percentage of non-developer users can complete Hero Workflow 1 end-to-end in <10 minutes with acceptable satisfaction (≥4/5)?

**Methodology**:
- **Phase 2 Usability Tests** (N=10): Moderated hero workflow testing sessions
  - 5 tests with Kit User personas (non-developers: marketers, PMs, founders)
  - 5 tests with Kit Creator personas (to validate submission workflow)
- **Test protocol**: See `research-instruments.md` → Usability Test Protocol #1
- **Setup**: Provide mockup/prototype of marketplace homepage + sample kits
- **Observation**: Record time-to-completion, friction points, user satisfaction

**Success Criteria**:
- **Pass**: ≥75% of non-developer users complete Hero Workflow 1 in ≤10 minutes
- **Pass**: ≥70% rate experience ≥4/5 stars (satisfaction threshold)
- **Pass**: "Wow moment" observed in ≥60% of sessions ("I just saved 2 hours")

**Evidence to Collect**:
- Time-to-first-task (from landing on homepage to executing first task)
- Friction points (where users get stuck: GitHub fork, template customization, AI agent commands)
- Satisfaction ratings (1-5 scale)
- Verbatim quotes for "wow moments" or confusion

---

## Research Question 3 (P1): Which persona has highest retention and willingness-to-pay?

**Hypothesis**: Kit Users (Marcus, Lisa) have higher retention than Kit Creators (Sarah) because they derive immediate time-saving value.

**Research Question**: Which persona segment (Kit Creators vs. Kit Users vs. Startup Founders) shows highest D7/D30 retention and willingness-to-pay signals?

**Methodology**:
- **Phase 1 Interviews** (same N=20 as RQ1): Ask willingness-to-pay probes
  - "Would you pay for [premium feature]? How much?"
  - "What would make you use this weekly vs. once?"
- **Phase 3 Beta** (N=50+): Track behavioral retention by persona
  - Instrument D7, D30 retention by persona segment
  - Track repeat usage (kits forked per user per month)
  - Measure cross-side conversion (users → creators)

**Success Criteria**:
- **Pass**: Identify 1 persona with D7 retention ≥30% and D30 retention ≥20%
- **Pass**: ≥40% of interviews indicate willingness-to-pay for premium features (analytics, private kits)
- **Pass**: Clear ranking of personas by retention (e.g., "Kit Users > Startup Founders > Kit Creators")

**Evidence to Collect**:
- Interview responses to willingness-to-pay probes (price points, feature preferences)
- Behavioral data: D7/D30 retention, repeat usage, churn
- Persona-specific engagement patterns (kits forked, categories explored)

---

## Research Question 4 (P1): Can we achieve ≥80% cross-agent compatibility for kits?

**Hypothesis**: Kits can work across Claude Code, Cursor, and Copilot with ≥80% compatibility without modification.

**Research Question**: What percentage of kits work across ≥2 AI agents (Claude Code, Cursor, Copilot) without modification or with documented workarounds?

**Methodology**:
- **Phase 1 Technical Validation** (N=10 seed kits): Test each kit with 3 agents
  - Select 10 diverse kits (marketing, PM, legal, startup)
  - Run hero workflow with Claude Code, Cursor, and Copilot
  - Document agent-specific issues, workarounds, success rates
- **Protocol**: See `research-instruments.md` → Multi-Agent Compatibility Test #1

**Success Criteria**:
- **Pass**: ≥80% of tested kits work with Claude Code + Cursor without modification
- **Pass**: ≥60% of tested kits work with all 3 agents (Claude, Cursor, Copilot)
- **Pass**: Agent-specific issues are documentable with clear workarounds (<5 min to fix)

**Evidence to Collect**:
- Compatibility matrix (kit × agent → pass/fail/workaround)
- Agent-specific failure modes (command syntax, file access, etc.)
- Workaround documentation quality (time to apply, clarity)

---

## Research Question 5 (P2): Do users prefer curated collections or open browse for kit discovery?

**Hypothesis**: Non-developers prefer curated collections ("Editor's Choice") while developers prefer open browse/search.

**Research Question**: What percentage of users prefer curated collections vs. open browse/search, and does preference vary by persona?

**Methodology**:
- **Phase 2 Usability Tests** (same N=10 as RQ2): A/B test discovery UX
  - 5 users test curated collections homepage
  - 5 users test open browse/search homepage
  - Measure time-to-kit-selection, satisfaction, preference
- **Phase 3 Beta** (N=50+): Instrument discovery paths
  - Track % users who use curated vs. search vs. browse
  - Measure conversion rate by discovery path

**Success Criteria**:
- **Pass**: Identify discovery preference by persona with ≥60% consistency
- **Pass**: At least one discovery path has >15% conversion (visitor → fork)
- **Insight**: Clear recommendation for MVP discovery UX (curated, browse, or both)

**Evidence to Collect**:
- User preference ratings (curated vs. browse)
- Time-to-kit-selection by discovery method
- Conversion rates by discovery path (curated vs. search vs. browse)
- Persona-specific patterns (do marketers prefer curated? do PMs prefer search?)

---

## Research Question 6 (P2): Will supply-side (Kit Creators) materialize without incentives?

**Hypothesis**: We can recruit 10-15 early creators to seed the marketplace with 20-30 high-quality kits.

**Research Question**: Can we recruit 10-15 Kit Creators to publish high-quality kits within 4 weeks of launch, and what incentives are necessary?

**Methodology**:
- **Phase 1 Creator Outreach** (N=30 targets, goal N=15 recruited):
  - Identify 30 potential creators (marketing ops leads, PM influencers, developer advocates)
  - Direct outreach with personalized message + early access offer
  - Track response rate, acceptance rate, publication rate
- **Phase 1 Creator Interviews** (N=10): Ask about publishing motivations
  - "What would motivate you to publish a kit?"
  - "What friction prevents you from documenting your workflow?"
  - "Would reputation/stats incentivize you?"

**Success Criteria**:
- **Pass**: Recruit ≥10 creators who commit to publishing within 4 weeks
- **Pass**: ≥70% of recruited creators actually publish a kit (conversion rate)
- **Pass**: ≥50% of published kits meet quality standards (4-file structure, README, example use cases)

**Evidence to Collect**:
- Outreach response rate (% who reply to DM)
- Acceptance rate (% who commit to publishing)
- Publication rate (% who actually publish)
- Creator motivations (reputation, community, intrinsic, incentives needed)

---

## Research Question 7 (P3): Is creator reputation scoring necessary in MVP?

**Hypothesis**: Creator reputation scoring can be deferred to post-PMF; manual curation ("Editor's Choice") is sufficient for MVP.

**Research Question**: Do Kit Users rely on creator reputation scores, or are other quality signals (stars, forks, recency) sufficient in MVP?

**Methodology**:
- **Phase 2 Usability Tests** (same N=10 as RQ2): Show kit cards with/without reputation scores
  - 5 users see kit cards with reputation badges (Newcomer, Contributor, Expert)
  - 5 users see kit cards with only stars/forks/recency
  - Measure trust, selection behavior, satisfaction
- **Phase 1 Interviews** (same N=20 as RQ1): Ask about trust signals
  - "What makes you trust a template you've never used?"
  - "Would you care about creator reputation or just kit quality?"

**Success Criteria**:
- **Defer if**: <40% of users mention creator reputation as important trust signal
- **Build if**: ≥60% of users prefer kits from "Expert" creators even with lower stars/forks
- **Insight**: Clear recommendation to build in MVP or defer to post-PMF

**Evidence to Collect**:
- User preference for trust signals (reputation vs. stars vs. recency)
- Selection behavior (do users pick high-reputation creators over high-star kits?)
- Interview quotes about trust and quality assessment

---

## Research Question 8 (P3): Do network effects exist? (Does more supply drive more demand?)

**Hypothesis**: Network effects exist: each new kit drives 5+ new users; 10%+ of users become creators (cross-side conversion).

**Research Question**: What is the correlation (R²) between kit count and user signups, and what percentage of users convert to creators?

**Methodology**:
- **Phase 3 Beta** (N=50+ users, 20-30 kits, 6-8 weeks):
  - Launch with 20 seed kits, add 2-3 kits per week
  - Track user signups per week vs. kit count per week
  - Measure cross-side conversion (% users who fork ≥1 kit → submit ≥1 kit)
  - Calculate correlation: R² between kit growth and user growth

**Success Criteria**:
- **Pass**: R² > 0.4 correlation between kit count and user signups (network effects exist)
- **Pass**: ≥10% of users who fork ≥1 kit submit their own kit within 90 days
- **Insight**: Confirm two-sided marketplace flywheel (more kits → more users → more creators → more kits)

**Evidence to Collect**:
- Weekly user signups vs. weekly kit count (time series data)
- Cross-side conversion rate (user → creator)
- Creator-to-user ratio over time (target 1:10 to 1:20)

---

## Research Question 9 (Ongoing): Which distribution channel delivers highest-quality users?

**Hypothesis**: Product Hunt drives volume; communities (Twitter, Reddit) drive quality (higher D7 retention).

**Research Question**: Which distribution channel (Product Hunt, Twitter, Reddit, GitHub trending, SEO) delivers users with highest activation rate and D7 retention?

**Methodology**:
- **Phase 3 Multi-Channel Launch**:
  - Launch on Product Hunt (primary channel, Week 1)
  - Twitter campaign (Weeks 1-2)
  - Reddit engagement (r/ProductManagement, r/marketing, Weeks 2-3)
  - GitHub trending (seed kits as standalone repos, Weeks 1-4)
  - SEO content (long-form guides, Weeks 2-8)
- **Instrumentation**: UTM tracking + cohort analysis
  - Track activation rate (% who fork ≥1 kit) by channel
  - Track D7 retention by channel
  - Measure cost-per-activation by channel (time/money spent)

**Success Criteria**:
- **Pass**: Identify 1-2 channels with activation ≥15% AND D7 retention ≥30%
- **Pass**: Clear ranking of channels by quality (retention + engagement) vs. volume
- **Insight**: Prioritize high-quality channels post-launch; reduce investment in low-quality channels

**Evidence to Collect**:
- Signups by channel (UTM source)
- Activation rate by channel (% who fork ≥1 kit)
- D7/D30 retention by channel
- Cost-per-activation by channel (time/money invested)

---

## Consolidated Research Phases & Timeline

| Phase | Duration | Research Questions | Sample Size | Deliverables |
|-------|----------|-------------------|-------------|--------------|
| **Phase 1: Problem & Persona Validation** | 4 weeks | RQ1, RQ3, RQ4, RQ6 | N=20 interviews, N=10 seed kits, N=30 creator outreach | Interview synthesis, JTBD validation, persona ranking, creator pipeline |
| **Phase 2: Hero Workflow Validation** | 3 weeks | RQ2, RQ5, RQ7 | N=10 usability tests | TTFW validation, discovery UX recommendation, reputation scoring decision |
| **Phase 3: Channel & Network Effects Validation** | 6-8 weeks | RQ8, RQ9 | N=50+ beta users, 20-30 kits, 4 channels | Channel ranking, network effects confirmation, retention cohorts |

---

## PDCA Cycle Checkpoints

Each research phase ends with a **Plan-Do-Check-Act** decision gate (see `validation-checkpoints.md` for detailed criteria).

**Phase 1 → Phase 2 Gate**:
- **Check**: Do personas have real, frequent pain? (RQ1)
- **Check**: Can we recruit enough creators? (RQ6)
- **Check**: Is cross-agent compatibility feasible? (RQ4)
- **Decision**: Go (advance to Phase 2) / Pivot (adjust personas or JTBD) / Kill (pain insufficient)

**Phase 2 → Phase 3 Gate**:
- **Check**: Can Hero Workflow 1 be completed in <10 min? (RQ2)
- **Check**: Which persona has highest retention? (RQ3)
- **Check**: Which discovery UX works best? (RQ5)
- **Decision**: Go (launch beta) / Pivot (redesign UX) / Kill (TTFW unachievable)

**Phase 3 → Post-PMF Gate**:
- **Check**: Do network effects exist? (RQ8)
- **Check**: Which channels drive quality users? (RQ9)
- **Check**: Are marketplace metrics hitting thresholds? (D7 ≥30%, MAK ≥50)
- **Decision**: Scale (invest in growth) / Pivot (adjust positioning) / Kill (PMF not achieved)

---

## Next Steps

1. **Generate research instruments** (`research-instruments.md`): Interview guides, usability test protocols, survey templates
2. **Define validation checkpoints** (`validation-checkpoints.md`): Go/kill/pivot criteria for each PDCA gate
3. **Begin Phase 1 recruitment**: Screen and schedule 20 interviews + 30 creator outreach targets
4. **Instrument Phase 3 metrics**: Set up GitHub API sync, Vercel Analytics, UTM tracking
