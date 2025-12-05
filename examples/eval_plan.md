---
**Version**: 1.0.0  
**Date**: 2025-12-05  
**Model**: Claude Opus 4.5 (Thinking)  
**References**:  
- [refs/5_more/pmfkit_optimize_guide.md](../refs/5_more/pmfkit_optimize_guide.md) — Three-stage optimization pipeline (EVALUATE→SUGGEST→IMPROVE)  
- [refs/5_more/pmfkit_optimize_quick_ref.md](../refs/5_more/pmfkit_optimize_quick_ref.md) — Quick reference for evaluation methodology  
- [refs/5_more/pmfkit_optimize_code_examples.md](../refs/5_more/pmfkit_optimize_code_examples.md) — Implementation patterns  
---

# Evaluation: Example Plan Documents

## Overview

Two PMF research plans for **agentii-kit** at different abstraction levels:

| Version | Focus | Duration | Scope |
|---------|-------|----------|-------|
| **my-product_0_0_2** | Website/gallery PMF discovery | 16 weeks (4 phases) | End-user marketplace |
| **my-product_0_0_3** | Platform/marketplace infrastructure | 12+ weeks (3 phases) | Kit creator ecosystem |

Both demonstrate excellent application of the PMF-Kit research methodology.

---

# Evaluation: `my-product_0_0_2/specs/001-agentii-kit-pmf/plan.md`

## Rating: 9.5/10 — Exceptional PMF research plan

### ✅ Strengths

**1. Comprehensive Research Questions (lines 12-48)**
- 6 well-defined questions with explicit hypotheses
- Each question has measurable success thresholds (e.g., "70%+ of interviewed personas")
- Clear evidence sources specified (N=20 interviews, N=18 usability tests)

**2. Two-Sided Marketplace Rigor**
- Questions balanced across creators (Q1, Q4) and users (Q1, Q3)
- Network effects explicitly measured (Q5: R² > 0.6 correlation)
- Cross-side conversion tracked (10%+ users → creators)

**3. PDCA Cycle Implementation (lines 151-167, 229-244, 299-319)**
- Weekly Do/Check/Act rhythm for each phase
- Explicit checkpoints with adjustment triggers
- Mid-phase course correction built in

**4. Constitution Alignment (lines 63-80)**
- All 7 constitution principles explicitly checked ✅
- Methodology validation against PMF-Kit core principles
- Traceable to spec.md hypotheses

**5. Risk Mitigation (lines 425-459)**
- 4 specific risks with concrete mitigation strategies
- Fallback plans for each risk scenario
- Pivot options documented (e.g., GitHub barrier → web UI alternative)

**6. Budget & Resource Planning (lines 498-502)**
- Realistic budget: $2,400 total for Phases 1-3
- Incentive structure: $50/participant
- Tool stack specified (Zoom, Calendly, Notion, Typeform, Vercel)

**7. Success Criteria Table (lines 404-422)**
- Clear Go thresholds for each phase/question
- Quantified metrics (75%+ completion, >= 4.0 satisfaction)
- Phase-specific criteria enabling independent validation

### ⚠️ Issues

**Issue 1: Directory Path Inconsistency**

```
Line 65: alignment with agentii-kit constitution principles (.specify/memory/constitution.md)
Line 467: (.specify/memory/constitution.md) - DONE
Line 472: Run `.specify/scripts/bash/update-agent-context.sh`
```

Uses `.specify/` but should be `.pmf/` or `.agentii/` to match the kit's namespace (same issue as constitution.md).

**Issue 2: Missing /pmfkit.optimize Integration**

No reference to the EVALUATE→SUGGEST→IMPROVE optimization pipeline from `refs/5_more/`. Could strengthen:
- Phase 3 channel testing with prompt optimization
- Hypothesis refinement between phases

**Issue 3: Phase 3 Network Effects Measurement May Be Premature**

Requires R² > 0.6 correlation between kit count and user signups (line 324), but with only 10-15 seed kits, sample size may be insufficient for robust statistical correlation.

**Recommendation**: Lower threshold to R² > 0.4 for Phase 3, require R² > 0.6 only at scale (Phase 4+).

---

# Evaluation: `my-product_0_0_3/specs/001-kit-marketplace/plan.md`

## Rating: 8/10 — Solid platform research plan with structural gaps

### ✅ Strengths

**1. Multi-Agent Validation (lines 95-98)**
- H4.1 explicitly tests Claude Code + Cursor + Copilot compatibility
- Technical validation sessions integrated into Phase 1
- Agent-agnostic design principle validated empirically

**2. Hypothesis Cluster Organization**
- 5 hypothesis clusters (H1-H5) map cleanly to research questions
- Creator JTBD (H1.1-1.3) + User JTBD (H2.1-2.3) clearly separated
- Market signals (H3, H5) and technical feasibility (H4) distinct tracks

**3. Research Traceability Table (lines 225-235)**
- Direct mapping from spec.md → hypotheses → research questions → instruments → timeline
- Excellent for audit trail and stakeholder communication

**4. Tiered Phase Exit Criteria (lines 124-128)**
- Three outcomes defined: GO, PIVOT, NO-GO
- PIVOT specifically addresses 1-2 clusters needing refinement
- Strategic hold option for fundamental redesign

**5. Compressed Timeline**
- 4-week Phase 1 (vs. 6 weeks in 0_0_2)
- More aggressive for platform infrastructure focus
- Weekly PDCA table (lines 117-122) enables rapid iteration

### ⚠️ Issues

**Issue 1: Less Detailed Than 0_0_2**

| Dimension | my-product_0_0_2 | my-product_0_0_3 |
|-----------|------------------|------------------|
| Research Questions | 6 detailed with thresholds | 4 high-level |
| Risk Mitigation | 4 specific risks | Not documented |
| Budget | $2,400 specified | Not specified |
| Phase 3 Detail | 6 weeks with channel breakdown | 4-6 weeks, less granular |

**Issue 2: Constitution Reference Path Correct but Different**

```
Line 54: Verify alignment with agentii-kit principles (/.pmf/memory/constitution.md)
```

Uses `/.pmf/` which is correct for PMF-Kit parent, but 0_0_3's constitution uses `.agentii/` directory. Inconsistency between plan and constitution.

**Issue 3: Missing Network Effects Measurement**

Unlike 0_0_2 (Q5: R² > 0.6 correlation), 0_0_3 doesn't explicitly measure marketplace network effects. For a platform constitution, this is a gap.

**Issue 4: Phases 2-3 Underspecified**

Phase 2 (lines 140-168) and Phase 3 (lines 170-196) are marked as "post-Phase 1 contingent" but lack:
- Specific research activities
- PDCA rhythm for each phase
- Risk mitigation strategies

**Issue 5: Missing Budget and Incentive Structure**

No participant incentive or budget estimate. For 24+ interviews + 13-18 usability tests, this is a planning gap.

---

# Comparative Analysis

| Dimension | my-product_0_0_2 | my-product_0_0_3 |
|-----------|------------------|------------------|
| **Research Questions** | 6 (detailed) | 4 (high-level) |
| **Phases** | 4 (0-3), 16 weeks | 3 (1-3), 12+ weeks |
| **PDCA Detail** | Weekly rhythm per phase | Weekly table, less detail in Phase 2-3 |
| **Constitution Alignment** | 7 principles checked | 5 principles checked |
| **Risk Mitigation** | 4 risks documented | Not documented |
| **Budget** | $2,400 estimated | Not specified |
| **Network Effects** | Q5 with R² threshold | Not measured |
| **Multi-Agent Testing** | Not explicit | H4.1 explicit |
| **Namespace** | `.specify/` (incorrect) | `/.pmf/` (correct but inconsistent with constitution) |

---

# Recommendations

## For 0_0_2 (Website Plan)

| Priority | Action |
|----------|--------|
| **P1** | Fix directory paths: `.specify/` → `.pmf/` or `.agentii/` |
| **P2** | Add `/pmfkit.optimize` integration for Phase 3 channel optimization |
| **P2** | Lower Phase 3 network effects threshold (R² > 0.4) until scale achieved |
| **P3** | Add multi-agent compatibility testing (currently missing) |

## For 0_0_3 (Platform Plan)

| Priority | Action |
|----------|--------|
| **P1** | Add budget and incentive structure |
| **P1** | Expand Phase 2-3 with PDCA rhythm and specific activities |
| **P1** | Add risk mitigation section |
| **P2** | Add network effects measurement (Q5 equivalent) |
| **P2** | Align namespace with constitution (`.agentii/` vs `/.pmf/`) |
| **P3** | Match detail level of 0_0_2 research questions |

## Cross-Plan

These plans describe the **same project** (agentii-kit) but:
- 0_0_2 is more complete and production-ready
- 0_0_3 has unique multi-agent validation but needs more detail

Consider:
1. **Merge best practices**: Use 0_0_2 structure with 0_0_3's multi-agent testing
2. **Explicit relationship**: 0_0_3 could be a "Platform Validation" sub-plan of 0_0_2

---

# Alignment with `/pmfkit.optimize` Methodology

Both plans would benefit from integrating the optimization pipeline from `refs/5_more/`:

| Stage | Application |
|-------|-------------|
| **EVALUATE** | Use multi-judge evaluation for interview synthesis quality |
| **SUGGEST** | Apply diagnostic analysis to identify research gaps |
| **IMPROVE** | Optimize channel messaging using MIPROv2/TextGrad |
| **VALIDATE** | A/B test landing page copy before Phase 3 launch |
| **ITERATE** | Monitor Phase 3 metrics for degradation, trigger re-optimization |

Neither plan currently references this pipeline, which is a missed opportunity for hypothesis refinement and channel optimization.

---

# Verdict

| Plan | Rating | Summary |
|------|--------|---------|
| **0_0_2** | 9.5/10 | Exceptional PMF research plan with comprehensive detail, PDCA cycles, risk mitigation, and budget. Minor namespace issues. |
| **0_0_3** | 8/10 | Solid platform plan with strong multi-agent validation but underspecified Phases 2-3, missing budget and risk mitigation. |

**Winner for production use**: 0_0_2 — more complete, actionable, and ready for execution.

**0_0_3's unique contribution**: Multi-agent compatibility testing (H4.1) should be merged into 0_0_2.


# v0.0.97




# Evaluation: Agentii-Kit Marketplace Plan (v0.0.97) vs. [/refs/5_more/](cci:7://file:///Users/frank/kits/pmf-kit/refs/5_more:0:0-0:0) References

## Rating: 9.5/10 — Exceptional PMF research plan with strong optimization integration

---

## ✅ Strengths

| Aspect | Assessment |
|--------|------------|
| **Research Questions** | Excellent—9 prioritized questions with hypotheses, success thresholds, evidence sources, and document references |
| **PDCA Cycles** | Strong—Explicit Plan→Do→Check→Act rhythm at 4-week, 3-week, and 6-8-week intervals |
| **Phase Exit Criteria** | Comprehensive—GO/PIVOT/KILL decisions with quantified thresholds per phase |
| **Constitution Check** | Complete—All 10 principles explicitly verified with mappings to research questions |
| **Budget & Resources** | Detailed—$1,500 budget, team allocation table, tools/platforms listed |
| **Risk Mitigation** | Strong—6 risks with impact, mitigation, AND fallback plans |
| **Accountability** | Clear—Phase owners, checkpoint authority, weekly review attendance requirements |
| **Assumptions Table** | Complete—5 assumptions with impact, validation method, and contingency plans |

---

## ✅ Strong `/pmfkit.optimize` Integration

Unlike the earlier specs and constitutions, this plan **correctly integrates** the optimization pipeline in multiple places:

### 1. Risk Mitigation (Line 165)
```markdown
| **Low retention** (D7 <20%) | High | Run `/pmfkit.optimize` to refine UX/positioning; interview churned users; A/B test improvements |
```

### 2. Phase 3 Decision Gate (Lines 401-403)
```markdown
**Decision**:
- **SCALE**: PMF achieved → Invest in growth...
- **ITERATE**: Weak PMF signals → Run `/pmfkit.optimize` to refine hypotheses; A/B test UX improvements
- **PIVOT**: No PMF → Major pivot required
```

### 3. Next Steps – Failure Path (Lines 492-495)
```markdown
**If Phase 1 Fails**:
- Run `/pmfkit.optimize` to refine hypotheses
- Conduct 5-10 additional interviews with adjusted personas
```

### 4. Phase Transitions (Lines 497-500)
```markdown
**At Phase Transitions**:
- Run `/pmfkit.optimize` to refine personas, JTBD, and success metrics based on learnings
- Update constitution if thresholds need adjustment
```

**This is excellent**—the plan correctly positions `/pmfkit.optimize` as a tool for hypothesis refinement when data invalidates assumptions.

---

## ⚠️ Minor Gaps vs. [/refs/5_more/](cci:7://file:///Users/frank/kits/pmf-kit/refs/5_more:0:0-0:0) Optimization Pipeline

### 1. **Optimization Pipeline Stages Not Fully Specified**

The plan references `/pmfkit.optimize` but doesn't specify the **5-stage pipeline**:
- EVALUATE → SUGGEST → IMPROVE → VALIDATE → ITERATE

**Current**: Generic "run `/pmfkit.optimize` to refine hypotheses"

**Recommendation**: Expand to include specific stages:
```markdown
**If Phase 1 Fails**:
- Run `/pmfkit.optimize evaluate` — Score interview synthesis quality against rubric
- Run `/pmfkit.optimize suggest` — Generate persona refinement recommendations
- Run `/pmfkit.optimize improve` — Apply optimizations to interview guide
- Re-run 5-10 interviews with improved protocol
```

### 2. **Missing Multi-Judge Evaluation for Interview Synthesis**

The refs specify (pmfkit_optimize_guide.md lines 98-155):
- Multi-judge consensus for evaluation reliability
- Fleiss' kappa ≥ 0.4 inter-rater agreement
- Bradley-Terry aggregation

**Gap**: Interview synthesis (T1.14-T1.16) has no multi-reviewer validation methodology.

**Recommendation**: Add to Phase 1 synthesis tasks:
```markdown
- [ ] **T1.14** Create JTBD synthesis document → `research-artifacts/analysis/jtbd-synthesis.md`
  - **Validation**: 2+ team members independently code interviews; calculate inter-rater agreement ≥0.6
```

### 3. **Missing Failure Mode Detection for Research Quality**

The refs define 8 failure modes (pmfkit_optimize_quick_ref.md lines 112-123). Research synthesis could fail in analogous ways:

| Agentic Failure Mode | Research Equivalent |
|---------------------|---------------------|
| Hallucination | Synthesizing patterns not in data |
| Instruction Drift | Research questions diverge from spec hypotheses |
| Incomplete Response | Missing persona segments in synthesis |
| Format Violation | Metrics lack quantified thresholds |

**Recommendation**: Add to Phase 1 synthesis:
```markdown
### Phase 1 Synthesis Quality Checklist
- [ ] No patterns asserted without ≥3 supporting quotes
- [ ] All 3 personas represented in synthesis
- [ ] Metrics include quantified thresholds (not "most users")
- [ ] Cross-reference: Synthesis conclusions traceable to spec.md hypotheses
```

### 4. **Weekly PMF Review Could Include Optimization Cadence**

The Weekly PMF Review ritual (lines 413-427) is excellent but could integrate optimization triggers:

**Current**: Generic "learnings" and "decisions" sections

**Recommendation**: Add explicit optimization trigger:
```markdown
4. **Optimization Check** (5 min): 
   - Did any metric drop >10% from prior week? → Trigger `/pmfkit.optimize evaluate`
   - Did 2+ interviews contradict hypothesis? → Trigger `/pmfkit.optimize suggest`
```

### 5. **Phase 3 Channel Optimization Missing A/B Testing Details**

The refs emphasize A/B testing (pmfkit_optimize_quick_ref.md lines 386-416):
- Staged rollout (staging → 10% → 100%)
- Statistical significance (p < 0.05)
- Minimum samples per variant

**Gap**: Phase 3 channel testing (T3.5-T3.8) mentions UTM tracking but no A/B test methodology for messaging optimization.

**Recommendation**: Add to Phase 3:
```markdown
- [ ] **T3.14** [P] Run `/pmfkit.optimize validate` on landing page copy
  - Variants: Problem-led messaging vs. Solution-led messaging
  - Traffic split: 50/50 per channel
  - Success threshold: p < 0.05, ≥100 visitors per variant
```

---

## Specific Line-Level Issues

| Line | Issue | Severity |
|------|-------|----------|
| 165, 402, 493-494, 498 | `/pmfkit.optimize` referenced but 5-stage pipeline not specified | Low |
| 228-234 | Interview synthesis lacks multi-reviewer validation | Medium |
| 371-389 | Phase 3 behavioral tracking comprehensive, but missing A/B test protocol | Medium |
| 419-424 | Weekly review agenda excellent, could add optimization trigger | Low |

---

## ✅ What's Done Exceptionally Well

### 1. Comprehensive Risk Mitigation (Lines 156-166)

6 risks with **three-column structure**: Impact + Mitigation + Fallback

| Risk | Mitigation | Fallback |
|------|------------|----------|
| Participant recruitment fails | Increase incentive $50→$75 | Extend Phase 1 by 2 weeks |
| Cross-agent compatibility <80% | Document workarounds; lower to 70% | Build MVP for Claude Code only |
| Hero Workflow TTFW >10 min | Redesign friction; add tutorial | Pivot to developer-only audience |

This exceeds most plans which only have mitigation, not fallback.

### 2. Traceability to Research Instruments (Lines 26-78)

Every research question includes:
```markdown
- **See**: `research-questions.md` → RQ1 | `research-instruments.md` → Interview Guide #1
```

This creates an audit trail from plan → questions → instruments → artifacts.

### 3. Weekly PMF Review Ritual (Lines 413-427)

Matches PMF-Kit constitution requirement exactly:
- 45-minute cadence
- 5-section agenda (Metrics, Learnings, Blockers, Decisions, Next Week)
- Required attendees specified
- Output defined (dashboard + priorities + decisions)

### 4. Assumptions with Contingency Plans (Lines 451-459)

Full 4-column structure: Assumption | Impact if Invalid | Validation Method | Contingency Plan

This exceeds the spec.md assumptions section which had 3 columns.

---

## Verdict

| Category | Rating |
|----------|--------|
| **Research Questions** | ✅ Excellent—9 questions with full traceability |
| **PDCA Cycles** | ✅ Strong—3 phases with explicit gates |
| **Constitution Alignment** | ✅ Complete—All 10 principles verified |
| **Budget & Resources** | ✅ Detailed—$1,500, team allocation, tools |
| **Risk Mitigation** | ✅ Comprehensive—6 risks with fallbacks |
| **Optimization Integration** | ✅ Good—Referenced at phase transitions and failure paths |
| **Multi-Judge Evaluation** | ⚠️ Missing—Synthesis lacks multi-reviewer validation |
| **A/B Testing Protocol** | ⚠️ Partial—UTM tracking but no messaging optimization |

**Overall**: 9.5/10 — The strongest plan I've evaluated. Correctly positions `/pmfkit.optimize` at failure paths and phase transitions. Minor gaps in specifying the 5-stage pipeline and multi-judge evaluation for synthesis quality.

---

## Recommended Additions

| Priority | Action |
|----------|--------|
| **P1** | Add multi-reviewer validation to Phase 1 synthesis tasks |
| **P2** | Expand `/pmfkit.optimize` references to specify 5-stage pipeline |
| **P2** | Add A/B test protocol for Phase 3 messaging optimization |
| **P3** | Add optimization trigger to Weekly PMF Review agenda |
| **P3** | Add synthesis quality checklist (no hallucination, complete coverage) |