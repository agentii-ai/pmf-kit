# PMF Specification: agentii-kit Website

**Feature Branch**: `001-agentii-kit-pmf`
**Created**: 2025-12-04
**Status**: Draft
**Discovery Focus**: Job Kit Marketplace Platform

## Overview

**What we believe**: Knowledge workers using AI agents (Product Managers, Marketers, Legal Ops, Educators) need a curated marketplace to discover, share, and adopt structured workflow templates ("Job Kits") that extend spec-driven development beyond software engineering.

**Who we're solving for**: Two-sided marketplace - (1) Kit Creators: domain experts encoding best practices into AI-ready templates, and (2) Kit Users: professionals seeking proven workflows for their discipline.

**Why now**: The explosion of AI coding agents (Claude Code, Cursor, Copilot) proves spec-driven workflows work for software. GitHub Spec-Kit's success validates the architecture. But PMs, marketers, and other knowledge workers lack a discovery layer to find non-coding workflows. The Cursor Rules and Fabric pattern libraries show demand for shareable prompts, but they lack the full-stack governance model that makes Spec-Kit powerful.

---

## Personas & Segments *(mandatory)*

### Primary Persona 1: The Kit Creator (Sarah - Product Manager)

**Context**:
- **Role**: Senior Product Manager at Series B SaaS company (100-300 employees)
- **Company**: B2B SaaS (project management, analytics, or collaboration tools), post-PMF scaling phase
- **Team**: Works with engineering (10-15 devs), design (2-3), marketing (5), and executives
- **Tools they use**: Notion (docs), Figma (design), GitHub (engineering handoff), Claude Code (rapid prototyping), Google Docs (specs)
- **Success metric**: Ship 3-5 features per quarter that move core product metrics (activation, retention, revenue)

**Pain Profile**:
- **Top pain**: "Every new feature starts from a blank page. I waste 2-3 hours writing PRDs with the same structure every time, and half the time I forget critical sections (edge cases, success metrics, dependencies). Engineers come back with 10 questions because I underspecified."
- **Current workaround**: Copy-paste old PRDs, manually edit, cross-fingers that AI agent (Claude) remembers context. No structured handoff between spec → plan → tasks.
- **Willingness to try**: Actively searches for "PM templates," "PRD automation," and "AI for PMs" on Twitter and Reddit. Tried Notion templates but they're static. Heard about Spec-Kit from engineering team and wondered, "Why isn't there a PM version?"

### Primary Persona 2: The Kit User (Marcus - Growth Marketer)

**Context**:
- **Role**: Growth Marketing Lead at early-stage startup (seed to Series A, 10-50 employees)
- **Company**: B2C or PLG SaaS, limited marketing resources (team of 1-2 marketers)
- **Team**: Works with product (PM), engineering (for tracking/analytics), and freelance designers/copywriters
- **Tools they use**: HubSpot/Mailchimp (email), Google Ads, LinkedIn Ads, Mixpanel (analytics), ChatGPT/Claude (content generation)
- **Success metric**: Hit quarterly growth targets (e.g., 20% MRR growth, 30% increase in qualified leads)

**Pain Profile**:
- **Top pain**: "I need to run 5 marketing experiments per month (landing pages, ad campaigns, content). Each experiment requires a campaign brief, targeting strategy, creative specs, and success metrics. I spend more time planning than executing. My AI assistant helps with copy, but I still have to manually structure every workflow from scratch."
- **Current workaround**: Uses ChatGPT with saved prompts, copy-pastes into Google Docs, manually tracks experiments in Notion. No structured workflow - just winging it.
- **Willingness to try**: Subscribed to 3 "marketing AI" newsletters. Tried PromptBase but found prompts too generic. Wants something closer to "GitHub for marketing workflows" - structured, version-controlled, community-curated.

### Secondary Persona: The Kit Power User (Elena - Engineering Manager exploring PM workflows)

**Context**:
- **Role**: Engineering Manager or Staff Engineer transitioning toward product/leadership roles
- **Company**: Mid-to-large tech company (500+ employees), established product org
- **Team**: Manages 5-8 engineers, interfaces with PM and design regularly
- **Tools they use**: GitHub, Jira, Notion, Claude Code (already uses Spec-Kit for code)
- **Success metric**: Successfully ship cross-functional initiatives with clear specs and minimal rework

**Pain Profile**:
- **Top pain**: "I understand Spec-Kit for engineering, but when I write product specs or roadmaps, I start from scratch. I want the same structured workflow for PM work."
- **Current workaround**: Adapts Spec-Kit templates manually for PM use, but they're not a perfect fit. Knows there must be a better way.
- **Willingness to try**: Already a Spec-Kit power user. High trust in the methodology. Will adopt immediately if PM-Kit exists and is well-documented.

### Segment You're NOT Building For

- **Enterprise IT procurement teams**: We're PLG (product-led growth), not enterprise sales. No SSO, SOC2, or procurement workflows in MVP.
- **Individual hobbyists with no professional workflow pain**: Target is knowledge workers with recurring, structured work (PMs, marketers, educators). Not casual AI tinkerers.
- **Software engineers** (for coding kits): Spec-Kit already serves this audience. We focus on non-engineering knowledge work.

---

## Problems & Jobs-to-Be-Done (JTBD) *(mandatory)*

### Primary JTBD #1: Discover Proven Workflows for My Domain (Priority: P1)

**Job Story**: When I'm starting a new project or recurring task in my professional domain (PM, marketing, legal), I want to quickly find a structured workflow template that experts have validated, so I can avoid reinventing the wheel and start with best practices instead of a blank page.

**Current Workaround**: Google searches ("PM PRD template," "marketing campaign template"), PromptBase (generic prompts), Notion template gallery (static, not AI-ready), copy-pasting from past work.

**Frequency**: Weekly to monthly (every new project, campaign, or feature)

**Evidence of willingness-to-pay**:
- PromptBase has 50K+ users paying $3-10 per prompt despite low quality
- Notion template marketplace thrives (but lacks AI integration)
- "Cursor Rules" GitHub repos have 2K+ stars (community demand for shareable configs)
- Twitter/Reddit: recurring requests for "best PM templates," "marketing automation," "AI workflows for non-engineers"

**Success signal**: User finds a relevant kit, forks it to their own GitHub, and completes their first workflow within 15 minutes. They return the following week to browse for another kit.

### Primary JTBD #2: Share My Workflow So Others Can Benefit (Priority: P2)

**Job Story**: When I've developed a structured workflow that consistently delivers results in my domain, I want to package it as a reusable template and share it with my community, so I can establish thought leadership, get feedback, and help others avoid the mistakes I made.

**Current Workaround**: Write blog posts (no structured format), share Notion templates (static, hard to maintain), post Twitter threads (ephemeral, not reusable).

**Frequency**: Quarterly to annually (after refining a workflow through multiple iterations)

**Evidence of willingness-to-pay**:
- Creators on PromptBase list prompts for $5-20 (monetization signal)
- Gumroad: Notion template creators earn $100-10K/month
- GitHub: Developers share `.cursorrules` for community karma + portfolio building
- LinkedIn: "How I do X" posts by PMs and marketers get 10K+ views (demand for workflow sharing)

**Success signal**: Creator submits a kit, receives 10+ stars/forks within 2 weeks, and gets 3+ issues/PRs from community improving the kit. They're motivated to maintain and update it.

### Primary JTBD #3: Validate Kit Quality Before Investing Time (Priority: P3)

**Job Story**: When I'm evaluating whether to adopt a new workflow kit, I want to quickly assess its quality (completeness, clarity, community validation), so I can avoid wasting time on half-baked or untested templates.

**Current Workaround**: Trial-and-error (download template, try to use it, abandon if incomplete), rely on blog post comments or Twitter endorsements (low signal).

**Frequency**: Every time evaluating a new kit (before adoption decision)

**Evidence of willingness-to-pay**:
- GitHub stars/forks serve as social proof (users trust community validation)
- Product Hunt upvotes influence adoption decisions
- Reddit: "Has anyone tried X?" posts before adopting new tools
- Users abandon 70%+ of downloaded templates within first use (high cost of low quality)

**Success signal**: User reviews kit metadata (stars, forks, last updated, completeness score), reads 2-3 example use cases, and confidently decides "yes, adopt" or "no, skip" within 3 minutes.

---

## Hero Workflows *(mandatory)*

### Hero Workflow 1: Discover and Fork a Kit (User Journey)

**Why this workflow matters**: This is the core demand-side activation moment. If users can't quickly find and adopt a useful kit, the marketplace fails. Connects to JTBD #1 (Discover Proven Workflows).

**End-to-end flow**:

1. **Input**: User arrives at kits.agentii.ai with a specific problem (e.g., "I need a structured way to write marketing campaign briefs")
2. **Process**:
   - Browse homepage gallery (featured kits, categories: PM, Marketing, Legal, Edu)
   - Filter by domain (Marketing) or search ("campaign brief")
   - Click into "Marketing Campaign Kit" card
   - Review kit details: description, example outputs, GitHub stats (stars, forks), last updated date, quality score
   - Click "Fork to GitHub" (one-click fork to their GitHub account)
   - See "Quick Start" guide: how to use with Claude Code, Cursor, or other AI agents
3. **Output**: User has kit forked to their GitHub, understands how to initialize it locally, and completes their first workflow (campaign brief) within 15 minutes
4. **Success signal**: User thinks, "Wow, that saved me 2 hours of setup. I'll come back next time I need a workflow."

**TTFW (Time-to-First-Workflow) Target**: < 10 minutes from landing on site to completing first workflow using a forked kit

**Guardrails & Error Recovery**:
- **What breaks the workflow?**: No GitHub account, kit is outdated/broken, AI agent not installed, unclear instructions
- **How do users recover?**:
  - "No GitHub account" → Prompt to sign up via GitHub OAuth (seamless)
  - "Kit outdated" → Display "Last updated: 6 months ago" warning; suggest alternative kits
  - "AI agent not installed" → Quick Start guide links to agent installation docs
  - "Unclear instructions" → Community comments/issues section where users report problems
- **Backstop if kit fails**: Community comments expose quality issues; featured kits are manually curated to ensure high quality

### Hero Workflow 2: Submit and Share a Kit (Creator Journey)

**Why this workflow matters**: Supply-side activation. If creators can't easily submit high-quality kits, the marketplace has no inventory. Connects to JTBD #2 (Share My Workflow).

**End-to-end flow**:

1. **Input**: Creator has a validated workflow (e.g., PM PRD template) in a GitHub repo with `.specify/` structure
2. **Process**:
   - Navigate to kits.agentii.ai and click "Submit a Kit"
   - Authenticate via GitHub OAuth
   - Select the GitHub repo containing the kit
   - Fill out kit metadata form:
     - Kit name, description (1-2 sentences)
     - Category (PM, Marketing, Legal, Edu, Other)
     - Tags (e.g., "PRD," "feature specs," "AI-ready")
     - Example use case (optional but encouraged)
   - Preview kit card (how it will appear in gallery)
   - Submit for review (manual curation in MVP, automated later)
3. **Output**: Kit appears in "Pending Review" state in creator dashboard. After approval (24-48 hours), kit goes live in gallery with stats tracking (views, forks, stars)
4. **Success signal**: Creator receives notification "Your kit is live!" and sees 5+ forks within first week. They feel motivated to maintain and improve the kit.

**TTFW (Time-to-First-Kit-Submission) Target**: < 5 minutes from "Submit a Kit" button to submission confirmation (excluding review wait time)

**Guardrails & Error Recovery**:
- **What breaks the workflow?**: Repo doesn't have `.specify/` structure, repo is private, incomplete metadata, low-quality kit
- **How do users recover?**:
  - "No .specify/ structure" → Show validation error with link to "Kit Creation Guide"
  - "Private repo" → Prompt to make repo public or explain that private kits aren't supported yet
  - "Incomplete metadata" → Inline form validation (required fields highlighted)
  - "Low-quality kit" → Manual review rejects kit with feedback ("Missing documentation," "Template incomplete")
- **Backstop if creator disappears**: Forks preserve kit even if original creator deletes repo; community can adopt orphaned kits

---

## Success Metrics & PMF Signals *(mandatory)*

### Activation Metrics

- **Kit User Activation**: % of visitors who fork a kit within first session (Target: 15%+)
- **Kit Creator Activation**: % of GitHub-authenticated users who submit a kit within 7 days (Target: 5%+)
- **First Workflow Completion**: % of users who fork a kit and complete a workflow within 24 hours (Target: 60%+)

### Engagement Metrics

- **Weekly Active Kits**: Number of kits forked/used per week (Target: 50+ forks/week after 3 months)
- **Return Visitor Rate**: % of users who return to browse/fork additional kits within 30 days (Target: 40%+)
- **Kit Depth**: % of users who fork 2+ kits (indicates platform stickiness) (Target: 30%+)

### Retention Metrics

- **Day-7 Retention**: % of activated users (forked a kit) who return within 7 days (Target: 30%+)
- **Day-30 Retention**: % of activated users still active after 30 days (Target: 20%+)
- **Creator Retention**: % of kit creators who submit a second kit within 90 days (Target: 50%+)

### AI-Specific Metrics

- **Kit Usefulness**: User-reported rating (1-5 stars) on kit quality after first use (Target: 4.0+ average)
- **Kit Completion Rate**: % of forked kits where user completes at least one full workflow (Target: 70%+)
- **AI Agent Compatibility**: % of kits that work seamlessly with Claude Code, Cursor, Copilot (Target: 95%+)

### Marketplace-Specific Metrics

- **Supply Health**: Number of active kits in marketplace (Target: 20+ high-quality kits across 3+ domains within 6 months)
- **Supply Diversity**: % of kits outside PM/Eng domains (Marketing, Legal, Edu) (Target: 40%+)
- **Creator-to-User Ratio**: Ratio of kit creators to kit users (Target: 1:10 to 1:20, typical for marketplaces)
- **Cross-Side Conversion**: % of users who become creators (Target: 10%+)
- **Network Effects**: Correlation between kit count and user growth (Target: Each new kit drives 5+ new users)

### Business Metrics

- **Organic Growth**: % of new users from referral/word-of-mouth vs. paid channels (Target: 30%+)
- **Community Engagement**: GitHub stars, issues, PRs on featured kits (Target: 100+ total stars across top 10 kits)
- **Waitlist Conversion**: % of waitlist signups who activate after launch (Target: 40%+)
- **Willingness to Pay (Future)**: % of survey respondents indicating they'd pay for premium features (Target: 20%+)

### PMF Validation Threshold

- **Sean Ellis Test**: 40%+ of activated users would be "very disappointed" if agentii-kit disappeared (surveyed after 30 days)
- **Retention**: 30%+ D30 retention for activated users
- **NPS**: Net Promoter Score > 50 from activated users
- **Creator Satisfaction**: 70%+ of kit creators rate submission/maintenance experience 4+ stars
- **Community Validation**: 3+ unsolicited testimonials or case studies from power users within 6 months

---

## Constraints & Risks *(mandatory)*

### Technical Feasibility

- **GitHub API Rate Limits**: Free tier allows 60 requests/hour/IP. For indexing kits, we need authenticated API access (5000 requests/hour). Must implement caching and webhook-based updates to avoid rate limit issues.
- **Kit Quality Validation**: No automated way to validate kit completeness/quality in MVP. Manual curation required (10-15 min per kit review). Risk: doesn't scale beyond 50-100 kits without automation.
- **AI Agent Compatibility**: Kits must work with Claude Code, Cursor, Copilot, and other agents. Spec-Kit architecture is agent-agnostic, but community may submit agent-specific kits. Mitigation: Require kits to be agent-agnostic or clearly label agent requirements.
- **Performance**: Kit browsing must load < 2 seconds. GitHub API latency + image assets could slow page loads. Mitigation: Use Vercel CDN, aggressive caching, lazy-load images.

### Competitive Landscape

- **Direct competitors**:
  1. **PromptBase**: Marketplace for prompts (not structured workflows). Lacks governance, version control, community curation. Advantage: First-mover with 50K+ users. Weakness: Low quality, no GitHub integration.
  2. **Fabric (Daniel Miessler)**: Open-source prompt pattern library. Advantage: Strong community, well-documented. Weakness: Task-oriented (one-shot prompts), not project-oriented (full lifecycle workflows). No marketplace/discovery layer.
  3. **Cursor Rules Repos**: GitHub repos sharing `.cursorrules` configs. Advantage: Developer-friendly, native GitHub. Weakness: Scattered across repos, no central discovery, engineer-only audience.
  4. **Notion Template Gallery**: Popular for static templates. Advantage: Massive user base. Weakness: Not AI-ready, no version control, no community feedback loops.
  5. **Gumroad/Etsy (Template Sellers)**: Creators sell templates for $5-50. Advantage: Monetization. Weakness: No community curation, no GitHub integration, one-time download (no updates).

- **Why we're different**:
  - **GitHub-native**: Kits live in Git repos (version control, collaboration, issues/PRs). Not proprietary platform.
  - **Full-stack governance**: Not just prompts - complete `constitution.md`, `spec.md`, `plan.md`, `tasks.md` structure inherited from Spec-Kit.
  - **Community curation**: Quality standards enforced. Featured kits are manually reviewed. Stars/forks serve as social proof.
  - **Cross-domain**: Serve PMs, marketers, legal, educators - not just engineers.

- **Incumbent workaround**: Copy-paste from old work, Google search for templates, ChatGPT with ad-hoc prompts.

### Top 3 PMF Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **Cold Start Problem**: No kits → no users. No users → no kit creators. Classic two-sided marketplace chicken-and-egg. | High | **Seed supply first**: Manually create 10-15 high-quality kits (PM-Kit, Marketing-Kit, Legal-Kit) before public launch. Interview 20-30 domain experts to validate kit usefulness. Recruit 5-10 "founding creators" to submit kits pre-launch. |
| **Quality Death Spiral**: Low-quality kits drive away users → fewer users discourage creators → even lower quality submissions. | High | **Strict curation in MVP**: Manual review of all kits (24-48 hour turnaround). Reject incomplete/untested kits with constructive feedback. Feature only 4-5 star kits on homepage. Implement quality rubric (completeness, clarity, tested, differentiated). |
| **GitHub Barrier**: Target users (PMs, marketers) may lack GitHub fluency. Friction in forking/using kits could kill activation. | Medium | **Progressive disclosure**: Tier 1 (Browse without GitHub account). Tier 2 (One-click fork with GitHub OAuth - abstract complexity). Tier 3 (Advanced users can edit directly). Provide video walkthroughs: "How to use a kit in 2 minutes." Test with 10 non-technical users before launch. |

---

## Distribution & Adoption Hypotheses *(mandatory)*

### Primary Channel Hypothesis

- **Channel**: Product Hunt launch for early adopter visibility and community validation
- **Rationale**: PH reaches early adopters in tech/productivity space (PMs, marketers, founders). Strong overlap with target audience. Successful launch (200+ upvotes) generates press coverage, backlinks, and waitlist signups. Validates demand before heavy investment.
- **Success criterion**: Top 5 product of the day (200+ upvotes), 500+ waitlist signups, 50+ activated users (forked a kit) within first week

### Secondary Channels (Ordered by Priority)

1. **Twitter/X**: Problem-solution storytelling targeting PM and marketing communities. Key accounts: @lennysan, @SahilBloom, @heyrobinrender, @GrowthHackers. Tweet threads showing "How I used Marketing-Kit to save 5 hours on campaign planning." Target: 5K impressions/week, 50 clicks to site.
2. **Communities (Reddit, Indie Hackers, Hacker News)**: Direct engagement in r/ProductManagement, r/marketing, r/GrowthHacking, Indie Hackers forums. Share kits as "Show HN" posts. Target: 10-20 high-quality signups per post.
3. **Content Marketing**: Long-form guides showing hero workflow examples. SEO-optimized for "PM PRD template," "marketing campaign workflow," "AI for product managers." Publish on blog + syndicate to Medium, Dev.to. Target: 500 organic visits/month by month 6.
4. **GitHub Community**: Share on Awesome Lists (awesome-product-management, awesome-marketing), submit to GitHub Explore trending repos. Leverage existing Spec-Kit community (crosspost in discussions). Target: 100+ GitHub stars on featured kits within 3 months.

### Viral/Network Hypothesis

- **Does collaboration/sharing drive value?** Partially. Individual use is primary (user forks kit for personal work), but sharing drives discovery.
- **If yes**: Users share kits with teammates ("Check out this PM-Kit - it's way better than our old template"). Kit creators share their submissions on Twitter/LinkedIn for thought leadership. Each kit submission = micro-viral event (creator's network sees it). Target: 10% of users invite at least one colleague within 30 days.

### Early Adopter Profile

- **Who jumps at this first?**:
  - Frustrated PM/marketer power users already using AI agents (Claude, ChatGPT) but lacking structured workflows
  - Engineering Managers transitioning to PM roles (already familiar with Spec-Kit)
  - Indie founders wearing multiple hats (PM + marketing + ops) seeking efficiency
- **Where to find them?**:
  - Twitter: Follow threads tagged #PMLife, #GrowthMarketing, #IndieHackers
  - Reddit: r/ProductManagement (140K members), r/marketing (1M members), r/SideProject (200K)
  - Discord: Lenny's Newsletter community, Indie Hackers, Blogging for Devs
  - LinkedIn: PM and marketing influencer posts
- **How to activate them?**:
  - Direct outreach via DMs: "Hey [Name], saw your tweet about [problem]. Built a tool to solve it - would love your feedback."
  - Early access invites (waitlist → first 100 users get "Founding Member" badge)
  - High-touch onboarding: 15-min Zoom calls with first 20 users to walk through hero workflow
  - Feature their kits prominently if they become creators ("Featured Creator" badge)

---

## Success Criteria for Discovery Phase *(mandatory)*

Before proceeding to research planning, we consider discovery successful when:

- [x] **Persona Validation**: Reviewed constitution and reference docs (refs/overview.md, refs/competitors.md). Personas (Kit Creator, Kit User) feel distinct based on market research and competitive analysis. Secondary validation required: 10-15 customer interviews.
- [ ] **JTBD Clarity**: Top 3 JTBD defined (Discover Workflows, Share Workflows, Validate Quality). Need interviews to validate frequency and willingness-to-pay assumptions. Target: 70%+ of interviewees mention at least one JTBD unprompted.
- [ ] **Hero Workflow Buy-In**: Need 5-10 users to manually validate both hero workflows (Discover/Fork, Submit/Share) end-to-end. Success: Users complete workflow in < 10 minutes, report "wow moment."
- [x] **Metrics Feasibility**: All metrics are instrumentable via Vercel Analytics + GitHub API + Typeform surveys. Verified: Can track forks, stars, page views, conversions. No technical blockers.
- [x] **Risk Acknowledgment**: Top 3 risks stated (Cold Start, Quality Death Spiral, GitHub Barrier). Mitigations drafted. Need to test mitigation effectiveness (e.g., manual kit seeding, non-technical user testing).
- [x] **Go-to-Market Confidence**: Primary channel (Product Hunt) identified. Testable in < 2 weeks (create landing page, recruit beta testers, schedule PH launch). Secondary channels (Twitter, Reddit, Content) prioritized.

---

## Open Questions

1. **Kit Quality Threshold**: What is the minimum quality bar for a kit to be "good enough" for the marketplace? Should we require (a) all `.specify/` files complete, (b) at least one example use case, (c) community validation (5+ users tested it), or (d) creator reputation (submit 2 kits before auto-approval)? **Impact: High - affects supply quality and creator friction.**

2. **GitHub Fluency Assumption**: Can non-technical users (PMs, marketers) realistically fork GitHub repos and use kits with AI agents? Or is this too high a barrier? Should we build a web-based "Kit Runner" that abstracts GitHub entirely (higher dev cost, but lower user friction)? **Impact: High - affects activation rate and target market size.**

3. **Monetization Timing**: Should we introduce paid features (private kits, premium support, creator monetization) in MVP, or wait until post-PMF? Early monetization tests willingness-to-pay but may reduce adoption. **Impact: Medium - affects growth trajectory but not core validation.**

---

## AI Product References

**Products with similar hero workflows** (for pattern reference):
- **Notion Template Gallery**: Browse → Preview → Duplicate to workspace. Proven model: 10M+ users adopt templates. Weakness: Static, not AI-ready. We add: GitHub integration, version control, community curation.
- **PromptBase**: Browse → Buy prompt → Use in ChatGPT. Proven model: 50K+ users, $3-10 per prompt. Weakness: Low quality, no structure. We add: Full governance (constitution/spec/plan), free + open-source, community quality control.
- **GitHub Awesome Lists**: Browse → Star/fork repo → Use code. Proven model: Developers trust community curation. We adapt: Extend to non-engineering domains, add discovery UI (not just README lists).
- **Cursor**: IDE autocomplete → time savings in coding → adoption through dev community. We mirror: Structured workflows → time savings in knowledge work → adoption through domain communities (PM, marketing, etc.).

**Key PMF patterns we're following**:
- **Product-led growth (PLG)**: Free tier (browse/fork unlimited kits) drives self-serve discovery. Paid tier (future) for private kits, advanced features.
- **Community curation**: Quality emerges from stars/forks/issues, not top-down control. Featured kits are manually curated initially, algorithmic later.
- **GitHub-native distribution**: Kits live in users' repos (no lock-in). Platform is discovery layer, not walled garden. Reduces friction, increases trust.
- **Marketplace dynamics**: Balance supply (kit creators) and demand (kit users). Seed supply first (10-15 manual kits), then recruit creators, then scale users.

---

## Next Steps

**Immediate**: Run `/pmfkit.clarify` to resolve top 3 open questions (Kit Quality Threshold, GitHub Fluency Assumption, Monetization Timing)

**If clarification passes**: Run `/pmfkit.plan` to design research methodology (customer interviews, landing page test, prototype usability study) and validation experiments (hero workflow tests with 10-20 users)

**If risks are high**: Run targeted hero workflow validation interviews (5-10 non-technical users testing kit discovery/forking flow) before full research planning
