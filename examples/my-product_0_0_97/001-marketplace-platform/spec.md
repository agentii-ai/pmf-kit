# PMF Specification: Agentii-Kit Marketplace

**Feature Branch**: `001-marketplace-platform`
**Created**: 2025-12-05
**Status**: Draft
**Discovery Focus**: Open-source marketplace for AI-agent-ready job kits
**Owner**: Product Lead

## Overview

**What we believe**: Professionals across all domains (marketing, PM, legal, education) waste hours reinventing workflows that should be standardized, while spec-driven development methodology (proven in coding via spec-kit) can eliminate the "blank page problem" for ALL knowledge work—not just software.

**Who we're solving for**: Two-sided marketplace serving (1) Kit Creators: Domain experts who want to share reusable workflows, and (2) Kit Users: Professionals seeking structured, AI-agent-ready templates to accelerate their work.

**Why now**: The explosion of AI coding agents (Claude Code, Cursor, GitHub Copilot) has validated spec-driven workflows for developers. The ecosystem is ready for the same structured approach to extend beyond code to marketing, product management, legal, and other knowledge work domains.

---

## Personas & Segments *(mandatory)*

### Primary Persona 1: Kit Creator (Sarah, Marketing Ops Lead)

**Context**:
- **Role**: Senior Marketing Operations Lead at growth-stage SaaS (Series B, 200 employees)
- **Company**: B2B SaaS targeting mid-market, 200-500 employees
- **Team**: Manages 3-5 marketers; collaborates with product, sales, and design teams
- **Tools they use**: Notion (docs), Asana (project management), HubSpot (CRM), Figma (design), ChatGPT/Claude (content)
- **Success metric**: Launch 8-12 campaigns per quarter with consistent quality and minimal rework

**Pain Profile**:
- **Top pain**: "Every new campaign starts from scratch. We've done 50+ product launches, but there's no standardized workflow. I spend 2-3 hours setting up Notion docs, task boards, and templates each time—it's pure waste."
- **Pain frequency**: 2-3 hours per campaign setup, 8-12 campaigns/quarter = 24-36 hours/quarter wasted
- **Current workaround**: Copy-pasting old campaign folders, manually updating task lists, maintaining scattered "template" docs in Notion
- **Willingness to try**: Actively bookmarks "marketing playbook" resources on Twitter, buys Notion templates ($10-50), follows marketing ops communities

### Primary Persona 2: Kit User (Marcus, Product Manager)

**Context**:
- **Role**: Mid-level Product Manager at early-stage startup (Seed, 15-30 employees)
- **Company**: AI/ML SaaS targeting developers and data scientists
- **Team**: Works with 5-8 engineers, 1 designer, directly reports to CEO
- **Tools they use**: Linear (project management), Notion (docs), Figma (design), GitHub, Claude Code (coding assistance)
- **Success metric**: Ship 3-5 features per quarter; maintain <10% feature rework rate

**Pain Profile**:
- **Top pain**: "I've written 30+ PRDs, but every time I start a new one I stare at a blank page for 20 minutes. There's no structure. Half the time I forget critical sections like success metrics or edge cases, and engineering comes back with questions."
- **Pain frequency**: 2-3 hours per PRD (starting from blank page + rework), 3-5 PRDs/quarter = 9-15 hours/quarter wasted
- **Current workaround**: Google "PRD template", copy from old PRDs, manually ensure consistency
- **Willingness to try**: Actively searches for "PM templates", follows #ProductManagement Twitter, joins PM Slack/Discord communities

### Secondary Persona: Kit User (Lisa, Startup Founder)

**Context**:
- **Role**: First-time founder, solo/technical founder building AI product
- **Company**: Pre-seed, bootstrapped, 1-3 people
- **Team**: Solo or small team (technical co-founder + 1 contractor)
- **Tools they use**: Notion, GitHub, Claude Code, Vercel, social media for distribution
- **Success metric**: Launch MVP in 60-90 days, get first 100 users

**Pain Profile**:
- **Top pain**: "I'm technical but terrible at marketing, legal, and fundraising. I need playbooks for stuff I've never done before—like launching on Product Hunt or writing Terms of Service."
- **Pain frequency**: Weekly (encounters new non-technical task 1-2x/week)
- **Current workaround**: YouTube tutorials, Twitter threads, hiring expensive consultants for one-off tasks
- **Willingness to try**: Pays for courses ($50-500), hires consultants ($100-300/hour for simple tasks), desperate for "startup in a box" resources

### Segment You're NOT Building For

- **Enterprise IT procurement teams**: They need vendor management, compliance, and approval workflows that are organization-specific and not shareable as open-source templates
- **Individual hobbyists without professional pain**: Users casually exploring AI without real workflow bottlenecks (no willingness-to-pay signal)
- **Consultants selling proprietary methodologies**: Users who monetize their workflows as paid services (conflict with open-source model)

---

## Problems & Jobs-to-Be-Done (JTBD) *(mandatory)*

### Primary JTBD #1: Discover Pre-Built Workflow for My Job (Priority: P1)

**Job Story**: When I encounter a new project type I've done before (or seen others do), I want to find a proven, structured workflow template, so I can start execution immediately instead of reinventing structure from scratch.

**Current Workaround**: Google "X template" (e.g., "marketing campaign template"), browse Notion template galleries, copy-paste from old projects, ask colleagues for their docs

**Frequency**: Weekly for Kit Users (new project/campaign/feature), Monthly for Kit Creators (when they decide to share a workflow)

**Evidence of willingness-to-pay**:
- Notion templates sell for $5-50 per template on Gumroad/Notion marketplace
- PromptBase users pay $3-10 per prompt
- Courses teaching "playbooks" sell for $50-500
- Spec-kit GitHub repo has 5,000+ stars in 3 months (strong demand signal)

**Success signal**: User finds kit, forks it, and completes first task within 10 minutes

### Primary JTBD #2: Share My Workflow as a Reusable Kit (Priority: P2)

**Job Story**: When I've developed a proven workflow through repetition (10+ times), I want to package it as a reusable template for others, so I can reduce duplicate questions, build reputation, and contribute to my community.

**Current Workaround**: Write blog posts with loose guidelines, create Notion templates and share links, answer the same questions repeatedly in Slack/Discord

**Frequency**: Quarterly (after refining a workflow, creator decides to document and share)

**Evidence of willingness-to-pay**:
- Creators already spend 5-10 hours writing blog posts/docs for free (intrinsic motivation exists)
- Notion creators list 100+ templates (supply exists despite friction)
- Developer tool creators publish open-source tools for reputation/community building

**Success signal**: Creator publishes kit in <30 minutes, receives stars/forks, gets actionable feedback

### Primary JTBD #3: Validate Kit Works Across AI Agents (Priority: P3)

**Job Story**: When I create or use a kit, I want to know it works with my preferred AI agent (Claude Code, Cursor, Copilot, etc.), so I don't waste time debugging agent-specific issues mid-workflow.

**Current Workaround**: Trial and error—try the template with their agent, debug if it breaks, give up if too many issues

**Frequency**: Every time a kit is used or updated (weekly for active users)

**Evidence of willingness-to-pay**:
- Users switch AI agents frequently (Cursor → Claude Code migrations common)
- Developers pay $20-40/mo for AI agent subscriptions—multi-agent support protects that investment
- Cross-agent compatibility is a frequent complaint in AI agent communities

**Success signal**: Kit displays compatibility badges; user confidently chooses kit knowing it works with their agent

---

## Hero Workflows *(mandatory)*

### Hero Workflow 1: Discover and Fork a Kit

**Why this workflow matters**: This is the core value for Kit Users (JTBD #1)—going from "I need to do X" to "I'm executing X with a proven template" in under 10 minutes.

**End-to-end flow**:

1. **Input**: User has a job to do (e.g., "I need to launch a marketing campaign" or "I need to write a PRD")
2. **Process**:
   - Land on agentii-kit marketplace homepage
   - Browse categories (Marketing, Product, Legal, Startup, etc.) OR search by keyword
   - Click into a kit card (e.g., "Marketing Campaign Kit")
   - Review kit details: description, example use cases, compatibility badges, stars/forks
   - Click "Fork to GitHub" → one-click fork to user's GitHub account
   - Follow setup instructions (customize `constitution.md`, run AI agent commands)
3. **Output**: User has a forked GitHub repo with all 4 core files (`constitution.md`, `spec-template.md`, `plan-template.md`, `tasks-template.md`) pre-populated with structure
4. **Success signal**: User starts executing first task using AI agent within 10 minutes of landing on site ("Wow, I just saved 2 hours of setup time")

**TTFW (Time-to-First-Workflow) Target**: < 10 minutes from landing on homepage to first task execution

**Guardrails & Error Recovery**:
- **What breaks the workflow?**: Kit is incomplete (missing files), GitHub fork fails, AI agent isn't installed, user doesn't understand how to customize templates
- **How do users recover?**: Fallback to manual GitHub fork, link to AI agent setup docs, example customizations provided in kit README
- **What's the backstop if AI fails?**: User can manually edit template files (they're just Markdown)—no AI required for core value

### Hero Workflow 2: Publish a New Kit

**Why this workflow matters**: This is the core value for Kit Creators (JTBD #2)—enabling supply-side to easily contribute high-quality kits.

**End-to-end flow**:

1. **Input**: Creator has a proven workflow they've used 10+ times (e.g., "Product Hunt launch checklist")
2. **Process**:
   - Creator clicks "Submit a Kit" on marketplace homepage
   - Fills out kit metadata form: Title, Description, Category, Tags, GitHub repo URL
   - Platform validates: 4 core files present, README complete, license specified
   - Creator submits for listing (auto-approved if validation passes)
   - Kit appears in marketplace within 5 minutes
3. **Output**: Kit is live, discoverable via search/browse, Creator receives confirmation with kit URL
4. **Success signal**: Creator sees their kit appear in search results, receives first star/fork notification ("I just helped someone!")

**TTFW (Time-to-First-Workflow) Target**: < 5 minutes from "Submit a Kit" button to kit live in marketplace

**Guardrails & Error Recovery**:
- **What breaks the workflow?**: GitHub repo is private, missing required files, broken links in README
- **How do users recover?**: Validation errors show specific issues (e.g., "Missing plan-template.md"), Creator fixes and resubmits
- **What's the backstop if validation fails?**: Creator can manually fix GitHub repo, resubmit (no data loss)

---

## Success Metrics & PMF Signals *(mandatory)*

### Activation Metrics

- **≥15% of visitors complete Hero Workflow 1** (browse → fork kit) in first session
- **≥60% of users who fork a kit complete first task** within 24 hours (using AI agent)
- **≥40% of creators who submit a kit receive first star/fork** within 7 days

### Engagement Metrics

- **≥2 kits forked per active user per month** (repeat usage signal)
- **≥30% of users explore 2+ kit categories** within first 7 days (breadth of use cases)
- **≥50% of kit creators update their kit** within 90 days (ongoing maintenance)

### Retention Metrics

- **≥30% Day-7 retention** for users who fork a kit
- **≥20% Day-30 retention** for activated users
- **<5% monthly churn** for creators who receive engagement (stars/forks)

### AI-Specific Metrics

- **≥80% of kits display multi-agent compatibility** (tested with ≥2 agents)
- **≥4.0/5.0 average user rating** for kits (quality threshold)
- **≥70% of users report kit worked with their agent** without modification (cross-agent success)

### Business Metrics

- **≥40% indicate willingness to pay** for premium features (analytics, private kits) in surveys
- **LTV/CAC ratio ≥3:1** within 12 months (assumes future monetization)
- **Viral coefficient ≥0.3** (1 kit creator → 0.3 new kit creators via community)

### Marketplace Metrics

- **Creator-to-user ratio: 1:10 to 1:20** (healthy supply/demand balance)
- **Cross-side conversion: ≥10% of users become creators** within 90 days (engaged community)
- **Network effects: R² > 0.4 correlation** between kit count and user signups (more kits → more users)
- **Monthly Active Kits (MAK): ≥50 kits forked/downloaded** per month by month 6

### PMF Validation Threshold

- **Sean Ellis test: ≥40% would be "very disappointed"** without agentii-kit
- **Retention: ≥30% D30** for users who complete Hero Workflow 1
- **NPS: ≥50 from activated users** (kit users who fork ≥1 kit)
- **Creator satisfaction: ≥70% rate submission experience 4+ stars**

---

## Constraints & Risks *(mandatory)*

### Technical Feasibility

- **GitHub dependency**: Platform relies on GitHub for kit hosting, versioning, and forking—any GitHub downtime or policy changes impact us
- **Multi-agent compatibility variability**: AI agents have different command syntax and file access patterns—maintaining ≥80% cross-agent compatibility requires ongoing testing
- **Metadata sync latency**: Syncing kit data from GitHub (stars, commits, contributors) in real-time may require caching/polling (acceptable <5 min delay)

### Multi-Agent Compatibility

- **Target agents**: Claude Code (primary), Cursor (secondary), GitHub Copilot (tertiary), Windsurf/Qoder (stretch)
- **Compatibility threshold**: ≥80% of kits must work across Claude Code + Cursor without modification
- **Testing approach**:
  - Kit creators run test workflow with ≥2 agents before submission
  - Platform aggregates compatibility data and displays badges
  - Document agent-specific workarounds in kit README

### Competitive Landscape

- **Direct competitors**:
  - **Notion template galleries**: Closed ecosystem, not version-controlled, not AI-agent-ready
  - **Gumroad/Etsy template marketplaces**: Monetized but fragmented, no quality standards, no multi-agent support
  - **GitHub repos (scattered)**: Open-source but no discovery layer, no quality curation, inconsistent structure
  - **.cursorrules repositories**: Developer-focused only, no extension to other domains
- **Why we're different**:
  - **Open-source + discoverable**: Unlike Notion (closed) and Gumroad (paid), we're free and GitHub-native
  - **Structured consistency**: Unlike scattered GitHub repos, we enforce 4-file spec-driven architecture
  - **Multi-domain**: Unlike .cursorrules (dev-only), we serve marketing, PM, legal, education, etc.
- **Incumbent workaround**: Google search → copy-paste from blog posts or old projects → manual customization (no structure, high friction)

### Top 3 PMF Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **Kit quality is too variable** (low-quality kits pollute marketplace) | High | Enforce validation (4-file structure, README, license); add creator reputation scores; manual curation for "Editor's Choice" |
| **Supply-side fails to materialize** (not enough kit creators) | High | Seed marketplace with 20-30 high-quality kits created by team; recruit 10-15 early creators with direct outreach + incentives |
| **Users don't understand "fork to work" concept** (too technical for non-devs) | Medium | Add onboarding tutorial video; simplify language ("Make your own copy" instead of "Fork"); provide example customizations |

---

## Assumptions *(mandatory)*

| Assumption | Impact if Invalid | Validation Method |
|------------|-------------------|-------------------|
| **GitHub will remain free for public repos** | High | Monitor GitHub pricing announcements; have contingency plan for GitLab/Codeberg alternatives |
| **AI agents support structured file workflows** | High | Test Hero Workflow 1 with Claude Code, Cursor, Copilot before MVP launch |
| **Target users (PMs, marketers, lawyers) are GitHub-literate** | Medium | Conduct 10-15 usability tests with non-developers; measure % who can fork a repo |
| **Demand for templates is sustainable** (not a fad) | Medium | Track Notion/Gumroad marketplace trends; interview users about long-term workflow pain |
| **Spec-driven methodology adapts to non-coding domains** | High | Validate PMF-Kit use cases (marketing, PM, legal kits); measure user satisfaction |

---

## Non-Goals *(mandatory)*

**Not building in this phase**:
- **Automated quality checks**: Manual curation for MVP (auto-validation enforces file structure only)
- **Advanced search/filters**: Basic browse by category + simple keyword search only
- **User accounts/profiles**: GitHub OAuth for authentication; no custom user profiles or dashboards in MVP
- **Payment processing**: No monetization in MVP—focus on proving value before adding premium features
- **Private/team kits**: All kits are public and open-source in MVP; private repos deferred to post-PMF
- **Kit versioning UI**: Users manage versions via GitHub tags/releases; no platform UI for version comparison

**Not targeting**:
- **Enterprise IT teams**: They need org-specific compliance workflows that aren't shareable as open-source
- **Consultants selling proprietary IP**: Users who want to monetize their workflows as paid services (conflicts with open-source model)
- **Non-English markets**: MVP is English-only; internationalization deferred to post-PMF

**Deferred to post-PMF**:
- **Kit analytics for creators**: Usage stats, fork counts, user feedback—requires instrumentation and dashboards
- **Collaboration features**: Co-editing kits, team workspaces, commenting—requires user accounts and real-time sync
- **API access**: Programmatic kit submission/retrieval for integrations with other tools
- **Monetization**: Premium tier for creators (analytics, private kits), sponsorship/ads

---

## Distribution & Adoption Hypotheses *(mandatory)*

### Primary Channel Hypothesis

- **Channel**: Product Hunt launch targeting early adopters in AI/developer/PM communities
- **Rationale**: Product Hunt reaches tech-savvy professionals who:
  - Understand GitHub workflows (low onboarding friction)
  - Actively use AI agents (primary use case)
  - Share discoveries in their communities (viral potential)
- **Success criterion**: 100+ high-quality signups (users who fork ≥1 kit) in first week; #1-5 product of the day

### Secondary Channels (Ordered by Priority)

1. **Twitter/X**: Problem-solution storytelling with real examples ("I built a marketing kit and saved 10 hours this week")—targeting #ProductManagement, #Marketing, #AITools communities
2. **Reddit communities**: Direct engagement in r/ProductManagement, r/marketing, r/LegalAdvice with "I made this" posts (provide genuine value, not spammy)
3. **GitHub trending**: Seed initial kits as standalone GitHub repos that can trend independently, driving traffic back to marketplace
4. **Content/SEO**: Long-form guides showing Hero Workflow 1 in action (e.g., "How to write a PRD in 10 minutes using agentii-kit")—targeting high-intent searches

### Viral/Network Hypothesis

- **Does collaboration/sharing drive value?** Yes—creators who publish kits invite their communities to use them (one creator can bring 10-50 users)
- **Mechanism**:
  - Creators share kit links on Twitter/LinkedIn/communities → users discover marketplace
  - Users fork kits, customize, and become creators themselves (cross-side conversion)
  - Kit pages show "View on GitHub" prominently → drives GitHub stars → drives trending → drives discoverability

### Early Adopter Profile

- **Who jumps at this first?**
  - **Frustrated power users**: PMs/marketers/ops leads who've built workflows 10+ times and are tired of copy-pasting
  - **AI agent enthusiasts**: Users actively experimenting with Claude Code/Cursor and looking for structured use cases
  - **Open-source advocates**: Users philosophically aligned with "fork to work" vs. walled gardens like Notion
- **Where to find them?**:
  - Twitter: #BuildInPublic, #ProductManagement, #AITools, #OpenSource
  - Reddit: r/ProductManagement, r/marketing, r/SideProject, r/MachineLearning
  - Discord: AI agent communities (Claude, Cursor), PM communities, startup communities
- **How to activate them?**:
  - **Direct outreach**: DM 50-100 power users with personalized message + early access
  - **High-touch onboarding**: 1-on-1 calls with first 20 creators to understand friction points
  - **Showcase their work**: Feature early creators' kits prominently ("Editor's Choice") to incentivize participation

---

## Success Criteria for Discovery Phase *(mandatory)*

Before proceeding to research planning, we consider discovery successful when:

- [ ] **Persona Validation**: Conducted 15-20 interviews; Kit Creator and Kit User personas feel distinct and real
- [ ] **JTBD Clarity**: Top 3 JTBD consistently mentioned; evidence of willingness-to-pay signals in 50%+ of interviews
- [ ] **Hero Workflow Buy-In**: 8-10 users manually validated Hero Workflow 1 (discover + fork) end-to-end; "wow moment" observed in ≥70%
- [ ] **Metrics Feasibility**: Can instrument all success metrics (forks, retention, cross-agent compatibility) within our tech constraints (GitHub API, Vercel Analytics)
- [ ] **Risk Acknowledgment**: Top 3 risks explicitly stated; mitigation plans drafted and budgeted
- [ ] **Go-to-Market Confidence**: Product Hunt launch plan drafted; 20-30 seed kits ready; 10-15 early creators recruited

---

## Open Questions *(prioritized)*

| Priority | Question | Decision Owner | Resolve By |
|----------|----------|----------------|------------|
| P1 | **Is Hero Workflow 1 achievable in <10 minutes for non-developers?** (or closer to 20 minutes?) | Product Lead | Phase 1 Week 2 |
| P1 | **Which persona has highest willingness-to-pay and retention?** (Kit Creators vs. Kit Users vs. Startup Founders) | Research Lead | Phase 1 Week 4 |
| P1 | **Can we achieve ≥80% cross-agent compatibility?** (or is 60% more realistic given agent fragmentation?) | Eng Lead | Phase 1 Week 3 |
| P2 | **Do users prefer curated collections or open browse?** (impacts discovery UX) | Product Lead | Phase 2 |
| P2 | **Should we support private kits in MVP?** (trade-off: reduces scope but limits enterprise use cases) | Product Lead | Phase 2 Week 2 |
| P3 | **Is creator reputation scoring necessary in MVP?** (vs. deferring to post-PMF) | Product Lead | Post-Phase 2 |

---

## AI Product References

**Products with similar hero workflows** (for pattern reference):
- **GitHub**: Discover repo → fork → customize → contribute back (proven fork-based collaboration model)
- **Notion template gallery**: Browse templates → duplicate → customize (proven template marketplace, but closed ecosystem)
- **PromptBase**: Discover prompts → buy → use with AI (proven marketplace for AI assets, but monetized and fragmented)
- **Spec-kit**: Discover kit → install → generate spec/plan/tasks (proven spec-driven workflow for coding, but dev-only)

**Key PMF patterns we're following**:
- **Product-led growth (PLG)**: Free tier (all kits open-source) drives self-serve discovery; monetize premium features later (analytics, private kits)
- **Network effects**: More kits → more users → more creators → more kits (two-sided marketplace flywheel)
- **Community-driven curation**: Early adopters become evangelists; "Editor's Choice" showcases high-quality kits; reputation scores incentivize quality

---

## Constitution Alignment *(mandatory)*

Verify alignment with Agentii-Kit constitution principles (`.pmf/memory/constitution.md`):

- [x] **Principle I (Marketplace-First Thinking)**: Spec includes both Kit Creator and Kit User personas; success metrics track supply AND demand
- [x] **Principle II (Kit Quality Standards)**: Validation enforces 4-file structure, README, license, multi-agent compatibility
- [x] **Principle III (Provider Enablement)**: Hero Workflow 2 targets <5 min kit submission; validation tools planned
- [x] **Principle IV (Discovery & Curation)**: Hero Workflow 1 targets <10 min discovery; search/filter/category taxonomy planned
- [x] **Principle V (GitHub-Native Architecture)**: Kits live on GitHub; platform is discovery/curation layer only
- [x] **Principle VI (Multi-Agent Compatibility)**: ≥80% cross-agent compatibility threshold; compatibility badges displayed
- [x] **Principle VII ("Fork to Work" Philosophy)**: Hero Workflow 1 is "discover → fork → execute" (not "start from blank page")
- [x] **Principle VIII (Spec-Driven Workflow Consistency)**: All kits enforce 4-file architecture
- [x] **Principle IX (Namespace Isolation)**: Uses `agentiikits.*` commands (not `pmfkit.*` or `specify.*`)
- [x] **Principle X (Accessibility & Inclusivity)**: Spec targets non-developers (marketers, PMs, lawyers); language avoids jargon

---

## Next Steps

**Immediate**: Run `/pmfkit.clarify` to resolve P1 open questions (Hero Workflow 1 timing, persona prioritization, cross-agent compatibility feasibility)

**If clarification passes**: Run `/pmfkit.plan` to design:
- Technical architecture (web app, GitHub sync pipeline, search/filter implementation)
- Kit validation workflow (automated checks + manual curation)
- Marketplace metrics instrumentation (forks, retention, cross-agent compatibility tracking)

**If risks are high**: Run targeted Hero Workflow validation sessions (5-10 non-developers) to de-risk usability assumptions before full planning

**At phase transitions**: Run `/pmfkit.optimize` to refine personas, JTBD, and success metrics based on interview learnings
