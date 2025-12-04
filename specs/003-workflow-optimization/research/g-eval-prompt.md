# G-Eval Prompt Template for PMF-Kit Template Evaluation

**Version**: 1.0
**Created**: 2025-12-04
**Purpose**: Chain-of-thought evaluation prompt for LLM judges assessing PMF-Kit templates

---

## Overview

This prompt uses the G-Eval (arXiv:2310.05470) methodology - requesting step-by-step reasoning before scoring to improve evaluation reliability and explainability.

**Key Principles**:
1. **Think before scoring**: Request reasoning first, score second
2. **Evidence-based**: Require specific quotes and examples
3. **Calibrated**: Provide scoring guidelines and reference examples
4. **Explainable**: Capture the "why" behind each score

---

## G-Eval Prompt Template

### System Prompt

```
You are an expert evaluator specializing in product-market-fit (PMF) discovery workflows and documentation quality. You will assess PMF-Kit templates and outputs using a multi-dimensional rubric.

Your evaluation approach:
1. Read the content thoroughly
2. For each dimension, explain your reasoning step-by-step
3. Provide specific evidence (direct quotes) supporting your reasoning
4. Assign a numerical score (1-10 scale) based on guidelines
5. Calculate weighted contribution to overall score

Be rigorous, specific, and evidence-based. Avoid vague assessments.
```

### Evaluation Task Prompt

```
# Evaluation Task

Evaluate the following PMF-Kit template/output on these 8 dimensions using the rubric provided:

## Dimensions to Evaluate

1. **Correctness** (Weight: 25%) - Accuracy and logical validity
2. **Coherence** (Weight: 15%) - Logical flow and organization
3. **Instruction-Following** (Weight: 15%) - Adherence to requirements
4. **Completeness** (Weight: 12%) - Coverage and thoroughness
5. **Specificity** (Weight: 10%) - Concreteness and actionability
6. **Clarity** (Weight: 10%) - Readability and ease of understanding
7. **Actionability** (Weight: 8%) - Ease of translating to actions
8. **Policy-Adherence** (Weight: 5%) - Compliance with PMF-Kit principles

---

## Content to Evaluate

```
{TEMPLATE_CONTENT}
```

---

## Evaluation Rubric

{RUBRIC_CONTENT}

---

## Your Task

For EACH dimension above, provide your evaluation in this format:

### [Dimension Name] (Weight: X%)

**Step 1: Initial Analysis**
[Explain what you're looking for in this dimension for the given content]

**Step 2: Evidence Collection**
[Provide 3-5 specific quotes or examples from the content showing strengths/weaknesses]
- ✅ STRENGTH: "[Quote]" - [Why this is good]
- ⚠️  WEAKNESS: "[Quote]" - [What's problematic]
- ✅ STRENGTH: "[Quote]" - [Why this is good]

**Step 3: Reasoning**
[Explain your overall assessment based on the evidence. What patterns do you see? How does this compare to expectations for high-quality PMF content?]

**Step 4: Score Assignment**
- **Raw Score (1-10)**: [Your score]
- **Justification**: [Brief explanation of why this specific score]
- **Weighted Contribution**: [Score × Weight]

---

After evaluating all 8 dimensions, provide:

## Overall Assessment

**Weighted Overall Score**: [Sum of all weighted contributions] / 10.0

**Quality Category**:
- 9.0-10.0: Exceptional
- 7.5-8.9: Strong
- 6.0-7.4: Adequate
- 4.0-5.9: Weak
- 1.0-3.9: Poor

**Summary**: [2-3 sentences summarizing the overall quality]

**Top 3 Strengths**:
1. [Specific strength with evidence]
2. [Specific strength with evidence]
3. [Specific strength with evidence]

**Top 3 Improvement Opportunities**:
1. [Specific issue with suggested fix]
2. [Specific issue with suggested fix]
3. [Specific issue with suggested fix]

**Recommendation**: [Publish as-is / Minor revisions / Major revisions / Complete rework]
```

---

## Judge-Specific Calibration

### GPT-4o (Strict Judge)

**Calibration Instructions**:
```
You are a STRICT evaluator. Apply high standards consistently:
- Be critical of vague language and missing details
- Expect evidence for all claims
- Look for edge cases and comprehensive coverage
- Minor issues should lower scores noticeably
- Reserve 9-10 scores for truly exceptional work
```

### Claude 3.5 Sonnet (Balanced Judge)

**Calibration Instructions**:
```
You are a BALANCED evaluator. Apply reasonable standards:
- Consider the context and intended audience
- Recognize both strengths and weaknesses fairly
- Distinguish between minor and major issues
- Use the full scoring range appropriately
- Focus on practical utility and usability
```

### Gemini 2.0 Pro (Lenient Judge)

**Calibration Instructions**:
```
You are a LENIENT evaluator. Apply supportive standards:
- Recognize effort and partial completeness
- Focus on what's working well
- Only flag critical gaps that block usability
- Give credit for novel approaches
- Be generous with scores for adequate work
```

---

## Example Evaluation (Reference for Calibration)

### Content to Evaluate

```
### Primary JTBD #1: Evaluate Workflow Quality (Priority: P1)

**Job Story**: When I complete a PMF discovery workflow (spec, plan, tasks), I want to systematically evaluate output quality across multiple dimensions, so I can identify specific improvement areas with confidence rather than relying on subjective judgment.

**Current Workaround**: Manual review with team discussion; inconsistent evaluation criteria; reliance on individual expertise and "gut feel"

**Frequency**: After every major workflow execution (weekly to bi-weekly during active discovery)

**Evidence of willingness-to-pay**: Teams currently hire external consultants or dedicate senior staff time for quality reviews - indicating willingness to invest in systematic evaluation

**Success signal**: Clear, quantified scores across evaluation dimensions (e.g., "Spec completeness: 7/10, JTBD clarity: 8/10") with specific evidence for each rating
```

### Example Judge Response (Claude 3.5 Sonnet)

### Correctness (Weight: 25%)

**Step 1: Initial Analysis**
I'm evaluating whether the JTBD statement is factually accurate, logically sound, and supported by evidence. For a JTBD definition, this means checking: persona accuracy, problem framing, frequency claims, workaround description, and success criteria.

**Step 2: Evidence Collection**
- ✅ STRENGTH: "systematically evaluate output quality across multiple dimensions" - Specific, measurable goal
- ✅ STRENGTH: "Teams currently hire external consultants or dedicate senior staff time" - Concrete evidence of willingness-to-pay
- ✅ STRENGTH: "weekly to bi-weekly during active discovery" - Specific frequency with context
- ✅ STRENGTH: "Clear, quantified scores across evaluation dimensions (e.g., 'Spec completeness: 7/10')" - Concrete success signal with example
- ⚠️  MINOR: "Manual review with team discussion" - Could specify team roles for more precision

**Step 3: Reasoning**
The JTBD is well-structured and follows established frameworks (job story format). All key components are present: situation, motivation, desired outcome. The frequency is specific and contextualized. Evidence of willingness-to-pay is concrete (consultant hiring, staff time). Success signal includes quantifiable examples. Only minor improvement: could specify which team roles are involved in manual reviews.

**Step 4: Score Assignment**
- **Raw Score (1-10)**: 8.5
- **Justification**: Highly accurate and well-supported, with specific evidence. Minor opportunity for additional precision in workaround description doesn't significantly impact overall correctness.
- **Weighted Contribution**: 8.5 × 0.25 = 2.125

[... similar detailed analysis for other 7 dimensions ...]

### Overall Assessment

**Weighted Overall Score**: 8.3 / 10.0

**Quality Category**: Strong (7.5-8.9 range)

**Summary**: This JTBD definition demonstrates strong quality across all dimensions. It's specific, evidence-based, and actionable. The job story format is well-executed with concrete frequency, workaround, and success signals. Minor improvements in precision would elevate it to exceptional.

**Top 3 Strengths**:
1. **Specific Success Signal**: Provides quantified example ("Spec completeness: 7/10") rather than vague outcomes
2. **Strong Evidence**: Concrete willingness-to-pay indicators (consultant hiring, staff time dedication)
3. **Contextualized Frequency**: "weekly to bi-weekly during active discovery" is precise with situational context

**Top 3 Improvement Opportunities**:
1. **Workaround Precision**: Specify team roles (e.g., "Manual review with PM, researcher, and designer") for better understanding
2. **Alternative Success Signals**: Consider adding 1-2 alternative success criteria for different user segments
3. **Quantify Willingness-to-Pay**: Add specific cost/time data if available (e.g., "$5K/month on consultants")

**Recommendation**: Minor revisions recommended (the improvements are non-critical enhancements)

---

## Usage Notes

### When to Use This Prompt

- Evaluating completed specs, plans, or task documents
- Assessing template quality for optimization
- Establishing baseline scores for v0.0.3 templates
- Validating improvements after optimization

### Customization Points

1. **Content Section**: Replace `{TEMPLATE_CONTENT}` with actual content to evaluate
2. **Rubric Section**: Replace `{RUBRIC_CONTENT}` with full rubric or link to rubric doc
3. **Judge Calibration**: Select appropriate strictness level (strict/balanced/lenient)
4. **Dimensions**: Can remove or add dimensions based on evaluation focus

### Best Practices

1. **Consistency**: Use same prompt format across all evaluations for comparability
2. **Calibration**: Start with reference examples to calibrate LLM judge expectations
3. **Evidence**: Always require specific quotes - prevents hallucination and vagueness
4. **Multiple Judges**: Run 3+ judges (GPT-4o, Claude, Gemini) for reliability
5. **Iterative Refinement**: If judge outputs are inconsistent, refine calibration instructions

---

## Integration with Evaluation Engine

### Python Function Signature

```python
def evaluate_with_g_eval(
    content: str,
    rubric_path: str,
    judge_model: str = "claude-3-5-sonnet-20241022",
    strictness: str = "balanced",
    temperature: float = 0.3
) -> EvaluationResult:
    """
    Evaluate content using G-Eval chain-of-thought pattern.

    Args:
        content: Template or output to evaluate
        rubric_path: Path to evaluation rubric markdown
        judge_model: LLM model to use as judge
        strictness: 'strict', 'balanced', or 'lenient'
        temperature: LLM temperature (lower = more consistent)

    Returns:
        EvaluationResult with dimensional scores and evidence
    """
    pass
```

### Expected Output Format (JSON)

```json
{
  "content_id": "spec-template-v0.0.3",
  "judge_model": "claude-3-5-sonnet-20241022",
  "strictness": "balanced",
  "timestamp": "2025-12-04T20:30:00Z",
  "dimensions": [
    {
      "name": "Correctness",
      "weight": 0.25,
      "score": 8.5,
      "reasoning": "...",
      "evidence": ["✅ STRENGTH: ...", "⚠️ WEAKNESS: ..."],
      "weighted_contribution": 2.125
    },
    // ... 7 more dimensions
  ],
  "overall_score": 8.3,
  "quality_category": "Strong",
  "summary": "...",
  "strengths": ["...", "...", "..."],
  "improvements": ["...", "...", "..."],
  "recommendation": "Minor revisions recommended"
}
```

---

## Version History

- **v1.0** (2025-12-04): Initial G-Eval prompt template for PMF-Kit optimization MVP
