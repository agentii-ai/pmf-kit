#!/usr/bin/env python3
"""
PMF-Kit Optimize Command - MVP Prototype
==========================================

A demonstration of the /pmfkit.optimize command showing the 5-stage pipeline:
EVALUATE → SUGGEST → IMPROVE → VALIDATE → ITERATE

This is a simplified prototype using mock evaluations and rule-based suggestions.
Full implementation will integrate real LLM judges (GPT-4o, Claude, Gemini) and
optimization algorithms (MIPROv2, TextGrad).

Usage:
    python optimize_mvp.py <template_path> [--mode=evaluate|suggest|improve|full]

Example:
    python optimize_mvp.py ../spec.md --mode=full
"""

import argparse
import json
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple
from pathlib import Path


@dataclass
class DimensionScore:
    """Score for a single evaluation dimension"""
    name: str
    weight: float
    score: float
    reasoning: str
    evidence: List[str]

    @property
    def weighted_contribution(self) -> float:
        return self.score * self.weight


@dataclass
class EvaluationResult:
    """Complete evaluation result from multi-judge consensus"""
    content_id: str
    judge_model: str
    dimensions: List[DimensionScore]
    overall_score: float
    quality_category: str
    summary: str
    strengths: List[str]
    improvements: List[str]
    failure_modes: List[str]

    def to_dict(self) -> Dict:
        return {
            'content_id': self.content_id,
            'judge_model': self.judge_model,
            'dimensions': [asdict(d) for d in self.dimensions],
            'overall_score': self.overall_score,
            'quality_category': self.quality_category,
            'summary': self.summary,
            'strengths': self.strengths,
            'improvements': self.improvements,
            'failure_modes': self.failure_modes
        }


@dataclass
class Suggestion:
    """Actionable improvement suggestion"""
    rank: int
    impact_score: float
    dimension: str
    issue: str
    before: str
    after: str
    rationale: str


class TemplateEvaluator:
    """Mock template evaluator using rule-based scoring"""

    DIMENSIONS = [
        ("Correctness", 0.25),
        ("Coherence", 0.15),
        ("Instruction-Following", 0.15),
        ("Completeness", 0.12),
        ("Specificity", 0.10),
        ("Clarity", 0.10),
        ("Actionability", 0.08),
        ("Policy-Adherence", 0.05),
    ]

    def evaluate(self, content: str, content_id: str) -> EvaluationResult:
        """
        Evaluate template content (mock implementation)

        In production: This would call GPT-4o, Claude, and Gemini judges in parallel
        """
        print(f"\n🔍 Evaluating: {content_id}")
        print("   Running multi-judge consensus...")

        # Mock dimensional scoring (simplified rule-based)
        dimensions = []
        for name, weight in self.DIMENSIONS:
            score = self._score_dimension(name, content)
            dimensions.append(DimensionScore(
                name=name,
                weight=weight,
                score=score,
                reasoning=self._get_reasoning(name, score, content),
                evidence=self._get_evidence(name, content)
            ))

        # Calculate overall score
        overall_score = sum(d.weighted_contribution for d in dimensions)

        # Determine quality category
        if overall_score >= 9.0:
            quality_category = "Exceptional"
        elif overall_score >= 7.5:
            quality_category = "Strong"
        elif overall_score >= 6.0:
            quality_category = "Adequate"
        elif overall_score >= 4.0:
            quality_category = "Weak"
        else:
            quality_category = "Poor"

        # Identify strengths and improvements
        strengths = [
            f"{d.name}: {d.score:.1f}/10"
            for d in sorted(dimensions, key=lambda x: x.score, reverse=True)[:3]
        ]

        improvements = [
            f"{d.name}: {d.score:.1f}/10 (needs +{10-d.score:.1f})"
            for d in sorted(dimensions, key=lambda x: x.score)[:3]
        ]

        # Detect failure modes
        failure_modes = self._detect_failure_modes(dimensions, content)

        return EvaluationResult(
            content_id=content_id,
            judge_model="mock-consensus",
            dimensions=dimensions,
            overall_score=overall_score,
            quality_category=quality_category,
            summary=f"Template scored {overall_score:.1f}/10.0 ({quality_category} quality). "
                    f"Top strength: {dimensions[0].name}. Key improvement: {sorted(dimensions, key=lambda x: x.score)[0].name}.",
            strengths=strengths,
            improvements=improvements,
            failure_modes=failure_modes
        )

    def _score_dimension(self, dimension: str, content: str) -> float:
        """Mock scoring logic (rule-based approximation)"""
        # In production: This would be LLM judge scoring using G-Eval

        # Simple heuristics for demo
        word_count = len(content.split())
        has_examples = "e.g." in content or "Example:" in content
        has_numbers = any(char.isdigit() for char in content)
        has_structure = "##" in content or "**" in content

        # Base score
        score = 7.0

        # Dimension-specific adjustments
        if dimension == "Correctness":
            score += 0.5 if word_count > 100 else -0.5
        elif dimension == "Coherence":
            score += 0.5 if has_structure else -1.0
        elif dimension == "Completeness":
            score += 1.0 if has_examples else -1.5
        elif dimension == "Specificity":
            score += 0.8 if has_numbers else -1.0
        elif dimension == "Clarity":
            score += 0.5 if word_count < 500 else -0.5
        elif dimension == "Actionability":
            score += 1.0 if "step" in content.lower() or "action" in content.lower() else -1.0

        return max(1.0, min(10.0, score))

    def _get_reasoning(self, dimension: str, score: float, content: str) -> str:
        """Generate reasoning for score (mock)"""
        if score >= 8.0:
            return f"{dimension} is strong. Content demonstrates good quality in this area."
        elif score >= 6.0:
            return f"{dimension} is adequate but has room for improvement."
        else:
            return f"{dimension} needs significant improvement. Critical gaps detected."

    def _get_evidence(self, dimension: str, content: str) -> List[str]:
        """Extract evidence from content (mock)"""
        # In production: LLM extracts actual quotes
        lines = content.split('\n')
        evidence = []
        if len(lines) > 0:
            evidence.append(f"✓ Found: {lines[0][:60]}...")
        if "example" in content.lower():
            evidence.append("✓ Contains examples")
        return evidence[:3]

    def _detect_failure_modes(self, dimensions: List[DimensionScore], content: str) -> List[str]:
        """Detect common failure patterns"""
        failures = []

        for dim in dimensions:
            if dim.score < 7.0:
                if dim.name == "Completeness":
                    failures.append("INCOMPLETE: Missing required sections or details")
                elif dim.name == "Specificity":
                    failures.append("AMBIGUOUS_INSTRUCTIONS: Vague or abstract guidance")
                elif dim.name == "Clarity":
                    failures.append("UNCLEAR: Complex or confusing language")

        return failures


class SuggestionGenerator:
    """Generate ranked improvement suggestions based on evaluation"""

    def generate(self, evaluation: EvaluationResult) -> List[Suggestion]:
        """
        Generate 5-7 ranked suggestions (mock implementation)

        In production: Uses meta-prompting with Claude Sonnet
        """
        print("\n💡 Generating improvement suggestions...")

        suggestions = []

        # Generate suggestions for weakest dimensions
        weak_dimensions = sorted(
            evaluation.dimensions,
            key=lambda d: d.score
        )[:5]

        for i, dim in enumerate(weak_dimensions):
            impact_score = (10 - dim.score) * dim.weight * 10

            suggestion = Suggestion(
                rank=i + 1,
                impact_score=impact_score,
                dimension=dim.name,
                issue=self._identify_issue(dim),
                before=self._generate_before_example(dim),
                after=self._generate_after_example(dim),
                rationale=self._generate_rationale(dim)
            )
            suggestions.append(suggestion)

        return sorted(suggestions, key=lambda s: s.impact_score, reverse=True)

    def _identify_issue(self, dim: DimensionScore) -> str:
        """Identify specific issue for dimension"""
        if dim.name == "Completeness":
            return "Missing concrete examples and edge cases"
        elif dim.name == "Specificity":
            return "Vague metrics and success criteria"
        elif dim.name == "Actionability":
            return "Unclear steps and sequencing"
        elif dim.name == "Clarity":
            return "Complex language and jargon"
        else:
            return f"Needs improvement in {dim.name.lower()}"

    def _generate_before_example(self, dim: DimensionScore) -> str:
        """Generate before example"""
        if dim.name == "Completeness":
            return "Users need systematic evaluation"
        elif dim.name == "Specificity":
            return "Define clear metrics"
        elif dim.name == "Actionability":
            return "Review and decide"
        else:
            return f"Current {dim.name.lower()} approach"

    def _generate_after_example(self, dim: DimensionScore) -> str:
        """Generate after example"""
        if dim.name == "Completeness":
            return "Users need systematic evaluation (e.g., 'Spec completeness: 7/10, JTBD clarity: 8/10')"
        elif dim.name == "Specificity":
            return "Define metrics with thresholds (e.g., ≥40% activation, ≥4.2/5 satisfaction)"
        elif dim.name == "Actionability":
            return "Step 1: Review exit criteria. Step 2: Compare to thresholds. Step 3: Document decision."
        else:
            return f"Improved {dim.name.lower()} approach with specifics"

    def _generate_rationale(self, dim: DimensionScore) -> str:
        """Generate improvement rationale"""
        return f"Improving {dim.name.lower()} from {dim.score:.1f}/10 will increase overall quality by ~{((10-dim.score) * dim.weight):.1f} points"


def print_evaluation_report(result: EvaluationResult):
    """Pretty print evaluation results"""
    print("\n" + "="*70)
    print(f"📊 Evaluation Report: {result.content_id}")
    print("="*70)
    print(f"\n Overall Score: {result.overall_score:.1f}/10.0 ({result.quality_category})")
    print(f"\n Summary: {result.summary}")

    print("\n Dimensional Breakdown:")
    for dim in result.dimensions:
        emoji = "✅" if dim.score >= 7.5 else "⚠️ " if dim.score >= 6.0 else "❌"
        print(f"  {emoji} {dim.name:25s}: {dim.score:.1f}/10 (weighted: {dim.weighted_contribution:.2f})")

    print("\n Top 3 Strengths:")
    for i, strength in enumerate(result.strengths, 1):
        print(f"  {i}. {strength}")

    print("\n Top 3 Improvement Opportunities:")
    for i, improvement in enumerate(result.improvements, 1):
        print(f"  {i}. {improvement}")

    if result.failure_modes:
        print("\n Failure Modes Detected:")
        for mode in result.failure_modes:
            print(f"  🚨 {mode}")


def print_suggestions(suggestions: List[Suggestion]):
    """Pretty print improvement suggestions"""
    print("\n" + "="*70)
    print("💡 Improvement Suggestions (Ranked by Impact)")
    print("="*70)

    for suggestion in suggestions:
        print(f"\n #{suggestion.rank} [Impact: {suggestion.impact_score:.1f}] {suggestion.issue}")
        print(f"    Dimension: {suggestion.dimension}")
        print(f"    Before: \"{suggestion.before}\"")
        print(f"    After: \"{suggestion.after}\"")
        print(f"    Rationale: {suggestion.rationale}")


def optimize(template_path: str, mode: str = "full"):
    """Run optimization pipeline"""
    print(f"\n🚀 Starting /pmfkit.optimize")
    print(f"   Target: {template_path}")
    print(f"   Mode: {mode}")

    # Load template content
    try:
        with open(template_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"\n❌ Error: Template not found: {template_path}")
        return

    content_id = Path(template_path).name

    # Stage 1: EVALUATE
    evaluator = TemplateEvaluator()
    evaluation = evaluator.evaluate(content, content_id)
    print_evaluation_report(evaluation)

    if mode == "evaluate":
        print("\n✓ Evaluation complete (mode=evaluate)")
        return

    # Stage 2: SUGGEST
    generator = SuggestionGenerator()
    suggestions = generator.generate(evaluation)
    print_suggestions(suggestions)

    if mode == "suggest":
        print("\n✓ Suggestions generated (mode=suggest)")
        return

    # Stage 3: IMPROVE (simplified)
    print("\n" + "="*70)
    print("✨ Stage 3: IMPROVE")
    print("="*70)
    print("\n [MVP Limitation: Auto-apply not implemented]")
    print(" In production: Would apply top suggestions automatically")
    print(f"\n Recommended Actions:")
    print(f"  1. Manually apply top 3 suggestions")
    print(f"  2. Re-run /pmfkit.optimize to measure improvement")
    print(f"  3. Iterate until target quality reached")

    # Stage 4: VALIDATE (mock)
    if mode == "full":
        print("\n" + "="*70)
        print("✓ Stage 4: VALIDATE")
        print("="*70)
        print(f"\n [MVP Limitation: Validation not implemented]")
        print(f" In production: Would re-evaluate optimized template")
        print(f"\n Estimated Improvement: +{sum(s.impact_score for s in suggestions[:3]):.1f} points")
        print(f" (from {evaluation.overall_score:.1f}/10 → ~{min(10.0, evaluation.overall_score + 1.5):.1f}/10)")

    print("\n✅ Optimization complete!")
    print(f"\n Next Steps:")
    print(f"  - Review suggestions above")
    print(f"  - Apply high-impact improvements manually")
    print(f"  - Re-run: python optimize_mvp.py {template_path}")


def main():
    parser = argparse.ArgumentParser(
        description="PMF-Kit Optimize Command - MVP Prototype"
    )
    parser.add_argument(
        "template",
        help="Path to template file to optimize"
    )
    parser.add_argument(
        "--mode",
        choices=["evaluate", "suggest", "improve", "full"],
        default="full",
        help="Execution mode (default: full)"
    )

    args = parser.parse_args()
    optimize(args.template, args.mode)


if __name__ == "__main__":
    main()
