# PMF-Kit Template Evaluation Rubric

**Version**: 1.0
**Created**: 2025-12-04
**Purpose**: Multi-dimensional quality assessment for PMF-Kit templates and outputs

---

## Overview

This rubric evaluates PMF-Kit templates and their outputs across 8 key dimensions using a 10-point scale. Each dimension has a weight that contributes to the overall quality score.

**Scoring Scale**:
- **9-10**: Exceptional - Exceeds expectations, best-in-class quality
- **7-8**: Strong - Meets expectations with minor improvements possible
- **5-6**: Adequate - Functional but has notable gaps
- **3-4**: Weak - Significant improvements needed
- **1-2**: Poor - Does not meet basic requirements

---

## Evaluation Dimensions

### 1. Correctness (Weight: 25%)

**Definition**: Accuracy, factual correctness, and logical validity of content

**Evaluation Criteria**:
- ✅ All facts and claims are accurate and verifiable
- ✅ No logical errors or contradictions
- ✅ Recommendations are sound and evidence-based
- ✅ Technical details (if any) are precise
- ✅ No hallucinations or invented information

**Scoring Guidelines**:
- **9-10**: All content is accurate; no errors detected; claims have clear evidence
- **7-8**: Mostly accurate with 1-2 minor errors that don't affect core value
- **5-6**: Several inaccuracies or logical gaps that reduce reliability
- **3-4**: Significant errors that undermine trust in content
- **1-2**: Pervasive errors; content is unreliable

**Evidence to Capture**: Specific examples of correct or incorrect content

---

### 2. Coherence (Weight: 15%)

**Definition**: Logical flow, structure, and organization of information

**Evaluation Criteria**:
- ✅ Information flows logically from one section to next
- ✅ Clear hierarchy and structure
- ✅ Ideas build on each other progressively
- ✅ No abrupt jumps or missing connections
- ✅ Narrative is easy to follow

**Scoring Guidelines**:
- **9-10**: Perfect flow; each section naturally leads to next; highly readable
- **7-8**: Good flow with occasional minor transitions issues
- **5-6**: Adequate structure but some sections feel disconnected
- **3-4**: Poor organization; difficult to follow reasoning
- **1-2**: Chaotic structure; no clear flow

**Evidence to Capture**: Examples of good/poor transitions and structure

---

### 3. Instruction-Following (Weight: 15%)

**Definition**: Adherence to template requirements and constraints

**Evaluation Criteria**:
- ✅ All mandatory sections completed
- ✅ Follows specified format and structure
- ✅ Respects constraints (e.g., word limits, style guidelines)
- ✅ Uses required terminology and conventions
- ✅ Addresses all prompts and questions

**Scoring Guidelines**:
- **9-10**: Perfect adherence; all requirements met; exemplary execution
- **7-8**: Follows most requirements with 1-2 minor deviations
- **5-6**: Meets core requirements but misses several optional elements
- **3-4**: Significant gaps in following instructions
- **1-2**: Does not follow basic template structure

**Evidence to Capture**: Specific requirements met/missed

---

### 4. Completeness (Weight: 12%)

**Definition**: Coverage of necessary information and thoroughness

**Evaluation Criteria**:
- ✅ All essential information included
- ✅ No critical gaps or missing sections
- ✅ Sufficient detail for understanding and action
- ✅ Examples and evidence provided where needed
- ✅ Edge cases and alternatives considered

**Scoring Guidelines**:
- **9-10**: Comprehensive; anticipates and addresses all relevant aspects
- **7-8**: Complete with minor omissions that don't affect usability
- **5-6**: Core information present but missing important details
- **3-4**: Significant gaps that require user to seek additional information
- **1-2**: Severely incomplete; unusable without major additions

**Evidence to Capture**: Missing information or thorough coverage examples

---

### 5. Specificity (Weight: 10%)

**Definition**: Concreteness and actionability of guidance

**Evaluation Criteria**:
- ✅ Specific, concrete recommendations (not vague)
- ✅ Clear action items and next steps
- ✅ Quantifiable metrics and targets where appropriate
- ✅ Real examples provided (not just abstract concepts)
- ✅ Sufficient detail to execute without guessing

**Scoring Guidelines**:
- **9-10**: Highly specific; clear, actionable guidance with concrete examples
- **7-8**: Mostly specific with occasional vague statements
- **5-6**: Mix of specific and vague; requires interpretation
- **3-4**: Largely vague and abstract; low actionability
- **1-2**: Entirely vague; no concrete guidance

**Evidence to Capture**: Examples of specific vs. vague guidance

---

### 6. Clarity (Weight: 10%)

**Definition**: Readability, simplicity, and ease of understanding

**Evaluation Criteria**:
- ✅ Plain language (appropriate for target audience)
- ✅ Concepts explained clearly
- ✅ No unnecessary jargon
- ✅ Sentence structure is simple and direct
- ✅ Key points are easy to identify

**Scoring Guidelines**:
- **9-10**: Crystal clear; effortless to understand; excellent readability
- **7-8**: Clear with occasional complex phrasing
- **5-6**: Adequate clarity but requires careful reading
- **3-4**: Confusing in multiple places; difficult to understand
- **1-2**: Incomprehensible; severely unclear writing

**Evidence to Capture**: Examples of clear/unclear writing

---

### 7. Actionability (Weight: 8%)

**Definition**: Ease of translating content into concrete actions

**Evaluation Criteria**:
- ✅ Clear next steps defined
- ✅ Prioritized action items
- ✅ Success criteria for each action
- ✅ Resources and tools identified
- ✅ Timeline or sequencing provided

**Scoring Guidelines**:
- **9-10**: Immediately actionable; clear steps with priorities and criteria
- **7-8**: Actionable with minor gaps in execution details
- **5-6**: Somewhat actionable but requires additional planning
- **3-4**: Difficult to translate into actions without significant work
- **1-2**: No clear path to action

**Evidence to Capture**: Examples of actionable guidance

---

### 8. Policy-Adherence (Weight: 5%)

**Definition**: Compliance with PMF-Kit constitution and guidelines

**Evaluation Criteria**:
- ✅ Follows PMF-Kit principles (Specification-First, Customer-Evidence-Driven, etc.)
- ✅ Uses correct namespace (pmfkit.* not speckit.*)
- ✅ No implementation details in specifications
- ✅ Maintains technology-agnostic approach where required
- ✅ Respects kit isolation and extensibility principles

**Scoring Guidelines**:
- **9-10**: Perfect adherence to all PMF-Kit principles and guidelines
- **7-8**: Follows core principles with minor policy deviations
- **5-6**: Mostly compliant but misses several policy requirements
- **3-4**: Significant policy violations
- **1-2**: Does not follow PMF-Kit principles

**Evidence to Capture**: Policy compliance/violations

---

## Weighted Score Calculation

**Formula**:
```
Overall Score = (Correctness × 0.25) + (Coherence × 0.15) +
                (Instruction-Following × 0.15) + (Completeness × 0.12) +
                (Specificity × 0.10) + (Clarity × 0.10) +
                (Actionability × 0.08) + (Policy-Adherence × 0.05)
```

**Interpretation**:
- **9.0-10.0**: Exceptional quality - Publish as reference example
- **7.5-8.9**: Strong quality - Minor refinements recommended
- **6.0-7.4**: Adequate quality - Notable improvements needed
- **4.0-5.9**: Weak quality - Major revisions required
- **1.0-3.9**: Poor quality - Requires complete rework

---

## Usage Guidelines

### For Human Evaluators

1. Read the template/output completely before scoring
2. Score each dimension independently (avoid halo effects)
3. Provide specific evidence for each score
4. Capture direct quotes showing strengths/weaknesses
5. Consider target audience and use case context
6. Be consistent across multiple evaluations

### For LLM Judges

1. Use G-Eval chain-of-thought pattern:
   - First, explain your reasoning for the dimension
   - Provide specific evidence (quotes from text)
   - Then assign a numerical score
2. Calibrate against reference examples if available
3. Be strict but fair in evaluation
4. Capture verbatim text as evidence

### Example Evaluation Entry

```json
{
  "dimension": "Correctness",
  "score": 8.5,
  "weight": 0.25,
  "reasoning": "The spec accurately describes PMF discovery workflows with evidence-based recommendations. All claims about JTBD validation are supported by research references. Minor issue: One metric (activation rate) lacks source citation.",
  "evidence": [
    "✅ Quote: '70%+ personas report pain frequency 2+x/week' - specific and measurable",
    "⚠️  Quote: 'activation 15%+' - no source provided for this benchmark"
  ],
  "weighted_contribution": 2.125
}
```

---

## Calibration Examples

### High-Quality Example (Score: 9.0)

**Persona Definition from spec.md**:
```
### Primary Persona: PMF Product Manager

**Context**:
- **Role**: Product Manager leading PMF discovery for AI SaaS startup
- **Company**: Seed to Series A startup (5-20 person team), AI/LLM product
- **Team**: Works with founders, engineers, growth/marketing, and customer success
- **Tools they use**: PMF-Kit, Claude Code/GitHub Copilot, Notion/Linear, customer interview tools
- **Success metric**: Validated PMF hypotheses leading to measurable product improvements and customer adoption

**Pain Profile**:
- **Top pain**: Iterating on PMF research workflows is manual and time-consuming - unclear if spec quality, research methods, or task execution needs improvement (frequency: every sprint)
- **Current workaround**: Ad-hoc refinement based on intuition; manually reviewing outputs and rewriting prompts/specs without systematic measurement
- **Willingness to try**: Actively seeking structured approaches to improve research quality and reduce discovery cycle time
```

**Why 9.0**: Specific role, context, pain frequency, current workaround all clearly defined. Concrete and actionable.

### Low-Quality Example (Score: 3.5)

**Vague Problem Statement**:
```
Users need better tools for their work. Current solutions are not good enough. We should build something that helps them do things faster.
```

**Why 3.5**: No specificity (who? what work? which tools?), no evidence, vague ("better", "faster"), not actionable.

---

## Version History

- **v1.0** (2025-12-04): Initial rubric creation for PMF-Kit optimization MVP
