---
**Version**: 1.0.0  
**Date**: 2025-12-05  
**Model**: Claude Opus 4.5 (Thinking)  
**References**:  
- [refs/5_more/pmfkit_optimize_guide.md](../refs/5_more/pmfkit_optimize_guide.md) — Three-stage optimization pipeline (EVALUATE→SUGGEST→IMPROVE)  
- [refs/5_more/pmfkit_optimize_quick_ref.md](../refs/5_more/pmfkit_optimize_quick_ref.md) — Quick reference for evaluation methodology  
- [refs/5_more/pmfkit_optimize_code_examples.md](../refs/5_more/pmfkit_optimize_code_examples.md) — Implementation patterns  
---

# Evaluation: Example Spec Documents

## Overview

Two PMF specifications for **agentii-kit** with complementary focuses:

| Version | Focus | Personas | JTBD Count |
|---------|-------|----------|------------|
| **my-product_0_0_2** | Website/gallery for discovering kits | Kit Creator (Sarah PM), Kit User (Marcus Marketer), Power User (Elena EM) | 3 |
| **my-product_0_0_3** | Platform infrastructure for kit ecosystem | Domain Expert Creator, Professional Practitioner User | 3 |

Both demonstrate excellent application of PMF-Kit specification methodology.

---

# Evaluation: `my-product_0_0_2/specs/001-agentii-kit-pmf/spec.md`

## Rating: 9.5/10 — Exceptional PMF specification

### ✅ Strengths

**1. Rich Persona Development (lines 20-66)**
- 3 distinct personas with role, company, team, tools, success metrics
- Detailed pain profiles with verbatim quotes ("Every new feature starts from a blank page...")
- "Willingness to try" signals for each persona
- Explicit "NOT building for" segment (lines 62-66)

**2. JTBD with Evidence (lines 70-118)**
- 3 prioritized JTBDs (P1, P2, P3)
- Each includes: Job Story, Current Workaround, Frequency, Willingness-to-pay evidence
- Concrete success signals ("User finds a relevant kit, forks it... within 15 minutes")
- Market evidence cited (PromptBase 50K+ users, Cursor Rules 2K+ stars)

**3. Hero Workflows with TTFW Targets (lines 122-183)**
- 2 complete workflows: Discover/Fork (User) and Submit/Share (Creator)
- Explicit time targets: <10 min user, <5 min creator
- Guardrails & error recovery for each workflow
- Backstop mechanisms documented

**4. Comprehensive Metrics Framework (lines 186-234)**
- 5 metric categories: Activation, Engagement, Retention, AI-Specific, Marketplace
- Specific targets for each (e.g., "15%+ fork rate", "30%+ D7 retention")
- Sean Ellis test included (40% "very disappointed")
- Business metrics (organic growth, community engagement)

**5. Competitive Analysis (lines 246-261)**
- 5 direct competitors analyzed (PromptBase, Fabric, Cursor Rules, Notion, Gumroad)
- Clear differentiation: GitHub-native, full-stack governance, community curation, cross-domain
- Incumbent workarounds documented

**6. Risk Mitigation Table (lines 263-269)**
- Top 3 risks with impact levels
- Concrete mitigations (seed supply, strict curation, progressive disclosure)
- Cold start, quality spiral, GitHub barrier all addressed

**7. Distribution Strategy (lines 273-308)**
- Primary channel (Product Hunt) with success criteria
- 4 secondary channels prioritized
- Early adopter profile with activation tactics
- Viral/network hypothesis documented

### ⚠️ Issues

**Issue 1: Directory Path Inconsistency**

```
Line 158: GitHub repo with `.specify/` structure
Line 176: "No .specify/ structure"
```

Uses `.specify/` but should be `.pmf/` or `.agentii/` to match the kit's namespace.

**Issue 2: Missing Multi-Agent Compatibility Detail**

Line 210 mentions "95%+ AI Agent Compatibility" target but lacks:
- Which agents are tested
- How compatibility is validated
- Agent-specific workarounds

0_0_3's spec handles this better with explicit multi-agent testing.

**Issue 3: Open Questions Excellent but Could Use Priority**

3 open questions (lines 327-331) are well-framed but lack:
- Priority ordering
- Decision timeline
- Owner assignment

---

# Evaluation: `my-product_0_0_3/specs/001-kit-marketplace/spec.md`

## Rating: 8.5/10 — Solid platform specification with less persona depth

### ✅ Strengths

**1. Platform Vision Clarity (lines 8-14)**
- Clear mission statement for marketplace
- "Why now" with 3 market timing factors
- Explicit positioning as platform infrastructure vs. single kit

**2. Multi-Agent Compatibility Focus (lines 204-209)**
- Technical feasibility section addresses agent compatibility
- "Initial MVP supports 2 agents" — realistic scoping
- 95%+ first-run success target for kit parsing

**3. Assumptions Section (lines 278-284)**
- 4 explicit assumptions documented
- Dependencies on GitHub, AI agents, creator motivation
- Phase 2 roadmap for non-technical users

**4. JTBD #3: Customize & Iterate (lines 81-92)**
- Unique focus on customization workflow
- "Contribute improvements back" — community flywheel
- Success signal includes PR contribution

**5. Hero Workflow Time Targets**
- Creator: <30 min to publish (realistic for kit creation)
- User: <15 min discovery to execution
- Aligns with refs/competitors.md "Fork to Work" strategy

### ⚠️ Issues

**Issue 1: Less Detailed Personas**

| Dimension | my-product_0_0_2 | my-product_0_0_3 |
|-----------|------------------|------------------|
| Personas | 3 (Sarah, Marcus, Elena) | 2 (generic roles) |
| Pain quotes | Verbatim | Paraphrased |
| Willingness to try | Detailed signals | Brief |
| Tools used | Listed | Listed |

0_0_2's personas are more actionable for interview recruitment.

**Issue 2: Metrics Less Quantified**

0_0_3 metrics (lines 150-193) lack specific targets:
- "% of users who fork" — no target %
- "Day-7 / Day-30 retention" — no threshold

Compare to 0_0_2 which specifies "15%+ fork rate", "30%+ D7 retention".

**Issue 3: Missing Evidence of Willingness-to-Pay**

JTBD sections reference "evidence of willingness-to-pay" but cite:
- "Experts publish free on Medium"
- "High engagement with Product Hunt launches"

These are weaker signals than 0_0_2's "$3-10 per prompt on PromptBase".

**Issue 4: Risk Table Less Detailed**

0_0_3's risk table (lines 219-223) has:
- 3 risks (same count as 0_0_2)
- Less specific mitigations
- No impact severity levels

**Issue 5: Open Questions Need Decision Framework**

3 open questions (lines 272-274) are well-framed but:
- No priority order
- No decision criteria
- No owner/timeline

---

# Comparative Analysis

| Dimension | my-product_0_0_2 | my-product_0_0_3 |
|-----------|------------------|------------------|
| **Persona Depth** | 3 detailed with quotes | 2 generic |
| **JTBD Evidence** | Strong ($, market data) | Moderate (engagement signals) |
| **Hero Workflows** | 2 with TTFW targets | 2 with TTFW targets |
| **Metrics** | Quantified targets | Categories only |
| **Competitive Analysis** | 5 competitors detailed | 4 competitors brief |
| **Risk Mitigation** | 3 with impact levels | 3 without levels |
| **Multi-Agent** | 95% target, no detail | 2-agent MVP scope |
| **Assumptions** | Implicit | 4 explicit |
| **Namespace** | `.specify/` (incorrect) | Not specified |

---

# Alignment with Reference Materials

## refs/overview.md Alignment

| Concept | 0_0_2 Coverage | 0_0_3 Coverage |
|---------|----------------|----------------|
| 4-file architecture | ✅ Mentioned | ✅ Mentioned |
| PM-Kit concept | ✅ Primary persona | ✅ Example kit |
| Marketing-Kit | ✅ Secondary persona | ✅ Example kit |
| Legal-Kit | ✅ Referenced | ✅ Example kit |
| GitHub-native | ✅ Core principle | ✅ Core principle |

## refs/competitors.md Alignment

| Competitor | 0_0_2 | 0_0_3 |
|------------|-------|-------|
| Fabric | ✅ Analyzed | ✅ Mentioned |
| PromptBase | ✅ 50K users cited | ✅ Mentioned |
| Cursor Rules | ✅ 2K+ stars cited | ✅ Implied |
| Notion Templates | ✅ Analyzed | ✅ Analyzed |
| Gumroad | ✅ Analyzed | ✅ Mentioned |

## refs/5_more (pmfkit.optimize) Alignment

Neither spec references the optimization pipeline. Potential integration points:
- Hypothesis validation could use EVALUATE stage
- Metrics refinement could use SUGGEST stage
- Distribution testing could use IMPROVE/VALIDATE stages

---

# Recommendations

## For 0_0_2 (Website Spec)

| Priority | Action |
|----------|--------|
| **P1** | Fix directory paths: `.specify/` → `.pmf/` or `.agentii/` |
| **P2** | Add multi-agent compatibility detail (which agents, how tested) |
| **P2** | Prioritize open questions with decision timeline |
| **P3** | Add assumptions section (currently implicit) |

## For 0_0_3 (Platform Spec)

| Priority | Action |
|----------|--------|
| **P1** | Add quantified targets to metrics (e.g., "15%+ fork rate") |
| **P1** | Strengthen personas with verbatim quotes and specific roles |
| **P2** | Add willingness-to-pay evidence (pricing signals, market data) |
| **P2** | Add impact levels to risk table |
| **P3** | Prioritize open questions with decision framework |

## Cross-Spec

These specs describe the **same project** but:
- 0_0_2 is more complete and actionable for research
- 0_0_3 has unique value in assumptions and multi-agent focus

Consider:
1. **Merge strengths**: Use 0_0_2 personas + metrics with 0_0_3's assumptions + multi-agent detail
2. **Explicit inheritance**: 0_0_3 could reference 0_0_2 for persona details

---

# Verdict

| Spec | Rating | Summary |
|------|--------|---------|
| **0_0_2** | 9.5/10 | Exceptional PMF spec with rich personas, quantified metrics, detailed competitive analysis. Minor namespace issues. |
| **0_0_3** | 8.5/10 | Solid platform spec with good multi-agent focus and explicit assumptions. Needs stronger personas and quantified metrics. |

**Winner for production use**: 0_0_2 — more complete, actionable, and ready for research planning.

**0_0_3's unique contributions**: 
- Explicit assumptions section (should merge into 0_0_2)
- Multi-agent MVP scoping (should merge into 0_0_2)
- JTBD #3 customization focus (complements 0_0_2's discover/share focus)




# v0.0.97




# Evaluation: Agentii-Kit Marketplace Spec (v0.0.97) vs. [/refs/5_more/](cci:7://file:///Users/frank/kits/pmf-kit/refs/5_more:0:0-0:0) References

## Rating: 8.5/10 — Strong PMF spec with partial optimization integration

---

## ✅ Strengths

| Aspect | Assessment |
|--------|------------|
| **Two-Sided Personas** | Excellent—Kit Creator (Sarah) + Kit User (Marcus) + secondary (Lisa) with quantified pain profiles |
| **JTBD with Evidence** | Strong—3 prioritized JTBDs with frequency, current workarounds, and willingness-to-pay evidence |
| **Hero Workflows** | Excellent—Clear end-to-end flows with TTFW targets (<10 min, <5 min) and guardrails |
| **Quantified Metrics** | Comprehensive—Activation, Engagement, Retention, AI-specific, Business, and Marketplace metrics all defined |
| **PMF Validation** | Strong—Sean Ellis test (40%), D30 retention (30%), NPS (50) thresholds specified |
| **Assumptions Section** | Good—5 assumptions with impact and validation methods per PMF-Kit constitution requirements |
| **Non-Goals** | Clear—Explicit scope boundaries with "not building", "not targeting", and "deferred" categories |
| **Constitution Alignment** | Excellent—Lines 382-395 explicitly verify alignment with all 10 principles |

---

## ⚠️ Gaps vs. [/refs/5_more/](cci:7://file:///Users/frank/kits/pmf-kit/refs/5_more:0:0-0:0) Optimization Pipeline

### 1. **Partial `/pmfkit.optimize` Reference**

The spec mentions optimization at line 410:
```markdown
**At phase transitions**: Run `/pmfkit.optimize` to refine personas, JTBD, and success metrics based on interview learnings
```

**Gap**: This is a good start but doesn't reference the **5-stage pipeline** (EVALUATE→SUGGEST→IMPROVE→VALIDATE→ITERATE) from the Quick Ref. It's treated as a phase-transition activity rather than a continuous methodology.

**Recommendation**: Expand to include:
```markdown
**Optimization Pipeline**:
- `/pmfkit.optimize evaluate` — Score spec quality against rubric before planning
- `/pmfkit.optimize suggest` — Generate improvement recommendations from interview feedback
- `/pmfkit.optimize validate` — A/B test Hero Workflow messaging with users
```

### 2. **Missing Multi-Judge Evaluation for Spec Quality**

The refs specify evaluation should use:
- 3-5 LLM judges with different rubrics
- Fleiss' kappa ≥ 0.4 agreement threshold
- Multi-dimensional rubric (correctness, coherence, completeness, etc.)

**Gap**: The spec has no self-evaluation methodology. How do we know this spec is "ready" for planning?

**Recommendation**: Add to "Success Criteria for Discovery Phase":
```markdown
- [ ] **Spec Quality Score**: `/pmfkit.optimize evaluate` returns ≥0.7 overall score
- [ ] **Multi-Agent Review**: Spec reviewed by ≥2 AI agents with agreement threshold met
```

### 3. **Missing Failure Mode Taxonomy**

The Quick Ref defines 8 failure modes for agentic systems:
- Hallucination, Instruction Drift, Tool Misuse, Reasoning Error
- Format Violation, Incomplete Response, Goal Abandonment, Infinite Loop

**Gap**: The spec has "Guardrails & Error Recovery" for Hero Workflows (lines 145-148, 168-171) but no systematic failure taxonomy.

**Good start at line 145-148**:
```markdown
**Guardrails & Error Recovery**:
- **What breaks the workflow?**: Kit is incomplete (missing files), GitHub fork fails...
- **How do users recover?**: Fallback to manual GitHub fork...
```

**Recommendation**: Map to optimization pipeline failure modes:
```markdown
### Spec Failure Modes (for `/pmfkit.optimize evaluate`)
| Failure Mode | Spec Equivalent | Detection |
|--------------|-----------------|-----------|
| Incomplete Response | Missing persona details | Checklist validation |
| Instruction Drift | JTBD doesn't match persona pain | Cross-reference check |
| Format Violation | Metrics lack quantified thresholds | Schema validation |
```

### 4. **Missing Continuous Optimization Cadence**

The refs emphasize **weekly review rituals** and **continuous monitoring**:
- Weekly metrics review (10 min)
- Degradation detection triggers reoptimization
- A/B testing before major changes

**Gap**: The spec has "Success Criteria for Discovery Phase" (lines 341-350) as a one-time checklist, not a continuous process.

**Recommendation**: Add to Next Steps:
```markdown
### Weekly Discovery Review (per constitution)
1. **Interview Synthesis** (10 min): New quotes, pattern updates
2. **Metrics Check** (10 min): Which assumptions validated/invalidated?
3. **Spec Optimization** (10 min): Run `/pmfkit.optimize suggest` on learnings
4. **Next Week** (5 min): Interview schedule, blockers
```

### 5. **Multi-Agent Testing Not Detailed**

Lines 233-238 mention multi-agent compatibility:
```markdown
### Multi-Agent Compatibility
- **Target agents**: Claude Code (primary), Cursor (secondary), GitHub Copilot (tertiary)
- **Compatibility threshold**: ≥80% of kits must work across Claude Code + Cursor
- **Testing approach**: Kit creators run test workflow with ≥2 agents before submission
```

**Gap**: No reference to the evaluation methodology from refs (multi-judge, agreement thresholds, diagnostic feedback).

**Recommendation**: Add per Quick Ref lines 50-67:
```markdown
### Multi-Agent Evaluation Methodology
- Automated kit validation MUST use ≥2 LLM judges
- Inter-judge agreement MUST achieve Fleiss' kappa ≥ 0.4
- Failed validations MUST include diagnostic suggestions (per `/pmfkit.optimize suggest`)
```

---

## Specific Line-Level Issues

| Line | Issue | Severity |
|------|-------|----------|
| 401-410 | "Next Steps" references `/pmfkit.optimize` but only at phase transitions | Medium |
| 341-350 | Success criteria is one-time checklist, no iteration cadence | Medium |
| 233-238 | Multi-agent testing lacks evaluation methodology details | Medium |
| 382-395 | Constitution alignment checklist doesn't include Principle XI (missing in constitution too) | Low |

---

## ✅ What's Done Well (Beyond Requirements)

### Excellent Quantified Metrics (Lines 175-219)

The spec exceeds PMF-Kit requirements with comprehensive, measurable thresholds:

| Metric Category | Example Metric | Threshold |
|-----------------|----------------|-----------|
| Activation | Visitors completing Hero Workflow 1 | ≥15% |
| Engagement | Kits forked per active user/month | ≥2 |
| Retention | D7 retention for kit forkers | ≥30% |
| AI-Specific | Kits with multi-agent compatibility | ≥80% |
| Marketplace | Creator-to-user ratio | 1:10 to 1:20 |
| PMF Validation | Sean Ellis "very disappointed" | ≥40% |

This aligns perfectly with PMF-Kit constitution "Metric Quality" requirements (quantified thresholds, timeframes, correlation targets).

### Strong Assumptions Section (Lines 263-271)

Meets constitution requirement for assumptions with:
- Impact if invalidated (High/Medium)
- Validation method
- Contingency implied

### Excellent Non-Goals (Lines 275-294)

Three-tier structure:
1. **Not building in this phase** (scope)
2. **Not targeting** (personas)
3. **Deferred to post-PMF** (roadmap)

---

## Verdict

| Category | Rating |
|----------|--------|
| **Persona Depth** | ✅ Excellent—Quantified pain, frequency, workarounds |
| **JTBD Quality** | ✅ Strong—Evidence-based, prioritized |
| **Hero Workflows** | ✅ Excellent—TTFW targets, guardrails, error recovery |
| **Metrics** | ✅ Comprehensive—Exceeds requirements |
| **Optimization Integration** | ⚠️ Partial—Referenced but not methodologically detailed |
| **Continuous Improvement** | ⚠️ Missing—No weekly review cadence |
| **Multi-Agent Evaluation** | ⚠️ Partial—Thresholds defined, methodology missing |

**Overall**: 8.5/10 — One of the stronger specs I've evaluated. Main gap is expanding the `/pmfkit.optimize` integration from a phase-transition checkpoint to a continuous methodology per refs/5_more.

---

## Recommended Additions

| Priority | Action |
|----------|--------|
| **P1** | Expand `/pmfkit.optimize` reference to include 5-stage pipeline |
| **P2** | Add weekly discovery review ritual to Next Steps |
| **P2** | Add multi-agent evaluation methodology (judges, agreement thresholds) |
| **P3** | Add spec failure mode taxonomy mapped to optimization pipeline |