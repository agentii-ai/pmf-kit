"""
Failure Mode Detection and Classification

Identifies common failure patterns in PMF-Kit templates and outputs.

Tasks: T040-T042 (Failure mode classifier, LLM-based classification, root cause diagnosis)
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional
import re


class FailureMode(Enum):
    """Common template/output failure modes"""
    AMBIGUOUS_INSTRUCTIONS = "ambiguous_instructions"
    INSUFFICIENT_CONTEXT = "insufficient_context"
    FORMAT_VIOLATION = "format_violation"
    INSTRUCTION_DRIFT = "instruction_drift"
    INCOMPLETENESS = "incompleteness"
    POOR_EXAMPLES = "poor_examples"
    VAGUE_METRICS = "vague_metrics"
    MISSING_CONSTRAINTS = "missing_constraints"


@dataclass
class FailureClassification:
    """Classification of a detected failure"""
    mode: FailureMode
    confidence: float  # 0.0-1.0
    evidence: str  # Quote or example showing failure
    affected_dimensions: List[str]  # Which evaluation dimensions are impacted
    severity: str  # "minor" | "moderate" | "critical"
    description: str  # Human-readable explanation


@dataclass
class RootCauseAnalysis:
    """Root cause diagnosis for a failure"""
    failure_mode: FailureMode
    root_cause: str  # Why this failure occurred
    impact: str  # How it affects quality
    improvement_aspects: List[str]  # Which aspects to improve (8 aspects from plan.md)
    suggested_fixes: List[str]  # Specific improvement recommendations


class FailureClassifier:
    """
    Rule-based and pattern-based failure mode classifier.

    Uses heuristics to detect common failure patterns without requiring LLM calls.
    For more nuanced classification, use LLM-based classifier.
    """

    def __init__(self):
        # Patterns for each failure mode
        self.patterns = {
            FailureMode.AMBIGUOUS_INSTRUCTIONS: [
                r'\b(might|could|should consider|maybe|perhaps)\b',
                r'\b(unclear|ambiguous|vague)\b',
                r'\bfor example\b.*\bfor example\b',  # Multiple unclear examples
            ],
            FailureMode.INSUFFICIENT_CONTEXT: [
                r'\[INSERT.*\]',
                r'\[TODO.*\]',
                r'\[FILL IN.*\]',
                r'\.\.\.',
                r'as mentioned (above|earlier|before)',  # Reference to missing context
            ],
            FailureMode.FORMAT_VIOLATION: [
                r'^[^#]',  # Missing markdown headers
                r'```\s*$',  # Unclosed code blocks
                r'\[([^\]]+)\]\([^\)]*$',  # Broken markdown links
            ],
            FailureMode.INSTRUCTION_DRIFT: [
                r'\b(ignore|skip|omit) (the|this|that)\b',
                r'\bnot applicable\b',
                r'\bN/A\b',
            ],
            FailureMode.INCOMPLETENESS: [
                r'\b(incomplete|missing|not provided|not specified)\b',
                r'\[MISSING\]',
                r'^\s*$\n^\s*$\n^\s*$',  # Multiple blank lines (empty sections)
            ],
            FailureMode.POOR_EXAMPLES: [
                r'\bExample:?\s*(TBD|TODO|N/A)',
                r'\bFor example,?\s*\.\.\.',
                r'\be\.g\.,?\s*$',  # e.g. with nothing following
            ],
            FailureMode.VAGUE_METRICS: [
                r'\b(improve|increase|better|more|higher)\b(?!.*\d)',  # No numbers
                r'\b(clear|good|quality)\b(?!.*threshold)',  # No thresholds
                r'\bmetric\b(?!.*\d|.*threshold|.*target)',
            ],
            FailureMode.MISSING_CONSTRAINTS: [
                r'\bmust\b.*but\b(?!.*if|.*unless)',  # Must without conditions
                r'\brequired\b(?!.*when|.*if)',  # Required without constraints
            ]
        }

    def classify_content(self, content: str, dimensional_scores: Dict[str, float]) -> List[FailureClassification]:
        """
        Classify failures in template/output content.

        Args:
            content: Template or output text to analyze
            dimensional_scores: Scores on each dimension (helps prioritize failures)

        Returns:
            List of detected failures, ordered by severity
        """
        failures = []

        for mode, patterns in self.patterns.items():
            matches = self._find_pattern_matches(content, patterns)

            if matches:
                # Calculate confidence based on number of matches
                confidence = min(len(matches) * 0.2, 1.0)

                # Determine affected dimensions
                affected_dims = self._get_affected_dimensions(mode, dimensional_scores)

                # Determine severity based on dimensional impact
                severity = self._calculate_severity(mode, affected_dims, dimensional_scores)

                # Create classification
                failure = FailureClassification(
                    mode=mode,
                    confidence=confidence,
                    evidence=matches[0] if matches else "",
                    affected_dimensions=affected_dims,
                    severity=severity,
                    description=self._get_failure_description(mode)
                )
                failures.append(failure)

        # Sort by severity (critical first)
        severity_order = {"critical": 0, "moderate": 1, "minor": 2}
        failures.sort(key=lambda f: (severity_order[f.severity], -f.confidence))

        return failures

    def _find_pattern_matches(self, content: str, patterns: List[str]) -> List[str]:
        """Find all pattern matches in content"""
        matches = []
        for pattern in patterns:
            found = re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE)
            for match in found:
                # Get context around match (50 chars before/after)
                start = max(0, match.start() - 50)
                end = min(len(content), match.end() + 50)
                context = content[start:end].strip()
                matches.append(f"...{context}...")
                if len(matches) >= 3:  # Max 3 examples
                    break
            if len(matches) >= 3:
                break
        return matches

    def _get_affected_dimensions(self, mode: FailureMode, scores: Dict[str, float]) -> List[str]:
        """Determine which evaluation dimensions are affected by this failure mode"""
        # Map failure modes to primary affected dimensions
        dimension_map = {
            FailureMode.AMBIGUOUS_INSTRUCTIONS: ["clarity", "specificity", "actionability"],
            FailureMode.INSUFFICIENT_CONTEXT: ["completeness", "clarity"],
            FailureMode.FORMAT_VIOLATION: ["coherence", "clarity"],
            FailureMode.INSTRUCTION_DRIFT: ["instruction_following", "policy_adherence"],
            FailureMode.INCOMPLETENESS: ["completeness", "correctness"],
            FailureMode.POOR_EXAMPLES: ["clarity", "actionability"],
            FailureMode.VAGUE_METRICS: ["specificity", "actionability"],
            FailureMode.MISSING_CONSTRAINTS: ["specificity", "correctness"]
        }

        affected = dimension_map.get(mode, [])

        # Filter to dimensions with low scores (< 7.0)
        return [dim for dim in affected if scores.get(dim, 10.0) < 7.0]

    def _calculate_severity(
        self,
        mode: FailureMode,
        affected_dimensions: List[str],
        scores: Dict[str, float]
    ) -> str:
        """Calculate failure severity"""
        if not affected_dimensions:
            return "minor"

        # Get lowest score among affected dimensions
        min_score = min(scores.get(dim, 10.0) for dim in affected_dimensions)

        # Critical failures
        critical_modes = [
            FailureMode.INCOMPLETENESS,
            FailureMode.INSTRUCTION_DRIFT,
            FailureMode.FORMAT_VIOLATION
        ]

        if mode in critical_modes or min_score < 5.0:
            return "critical"
        elif min_score < 7.0:
            return "moderate"
        else:
            return "minor"

    def _get_failure_description(self, mode: FailureMode) -> str:
        """Get human-readable description of failure mode"""
        descriptions = {
            FailureMode.AMBIGUOUS_INSTRUCTIONS: "Instructions use vague or ambiguous language, making it unclear how to proceed",
            FailureMode.INSUFFICIENT_CONTEXT: "Missing context, placeholders, or references to undefined information",
            FailureMode.FORMAT_VIOLATION: "Content violates expected format or structure (markdown, sections, etc.)",
            FailureMode.INSTRUCTION_DRIFT: "Content deviates from or ignores template requirements",
            FailureMode.INCOMPLETENESS: "Missing required sections, information, or details",
            FailureMode.POOR_EXAMPLES: "Examples are missing, incomplete, or not helpful",
            FailureMode.VAGUE_METRICS: "Metrics and success criteria lack specific thresholds or targets",
            FailureMode.MISSING_CONSTRAINTS: "Requirements lack clear conditions, constraints, or boundaries"
        }
        return descriptions.get(mode, "Unknown failure mode")


def diagnose_root_cause(failure: FailureClassification) -> RootCauseAnalysis:
    """
    Perform root cause analysis for a detected failure.

    Args:
        failure: Classified failure mode

    Returns:
        RootCauseAnalysis with diagnosis and recommendations
    """
    # Map failure modes to root causes and improvement aspects
    root_cause_map = {
        FailureMode.AMBIGUOUS_INSTRUCTIONS: RootCauseAnalysis(
            failure_mode=failure.mode,
            root_cause="Instructions use subjective or ambiguous language instead of specific, actionable steps",
            impact="Users don't know exactly what to do; increases interpretation variance",
            improvement_aspects=["instruction_clarity", "constraint_specificity"],
            suggested_fixes=[
                "Replace subjective terms (good, clear, quality) with specific criteria",
                "Add numbered steps for complex processes",
                "Provide explicit definitions for key terms",
                "Include concrete examples for each instruction"
            ]
        ),

        FailureMode.INSUFFICIENT_CONTEXT: RootCauseAnalysis(
            failure_mode=failure.mode,
            root_cause="Template lacks necessary examples, definitions, or background information",
            impact="Users lack guidance; must infer missing information",
            improvement_aspects=["context_provision", "example_quality"],
            suggested_fixes=[
                "Add 2-3 in-context examples showing good/bad implementations",
                "Define all domain-specific terms in glossary",
                "Replace placeholders with concrete examples",
                "Add 'For example:' sections showing expected outputs"
            ]
        ),

        FailureMode.FORMAT_VIOLATION: RootCauseAnalysis(
            failure_mode=failure.mode,
            root_cause="Template doesn't specify output format clearly or examples violate format",
            impact="Outputs are inconsistent and hard to parse/use downstream",
            improvement_aspects=["format_specification", "example_quality"],
            suggested_fixes=[
                "Add explicit output format schema (JSON, YAML, markdown structure)",
                "Show before/after format examples",
                "Add validation rules for output format",
                "Include format checklist"
            ]
        ),

        FailureMode.INSTRUCTION_DRIFT: RootCauseAnalysis(
            failure_mode=failure.mode,
            root_cause="Template allows or encourages skipping required sections/constraints",
            impact="Outputs omit critical information; inconsistent quality",
            improvement_aspects=["instruction_clarity", "constraint_specificity"],
            suggested_fixes=[
                "Make all requirements explicit with 'MUST' language",
                "Add examples showing consequences of skipping sections",
                "Include completeness checklist",
                "Emphasize required vs. optional sections"
            ]
        ),

        FailureMode.INCOMPLETENESS: RootCauseAnalysis(
            failure_mode=failure.mode,
            root_cause="Template doesn't prompt for all necessary information",
            impact="Outputs lack critical details needed for downstream use",
            improvement_aspects=["instruction_clarity", "example_quality"],
            suggested_fixes=[
                "Add completeness checklist covering all required information",
                "Provide examples showing fully complete outputs",
                "Add prompting questions for each required section",
                "Specify minimum detail level for each section"
            ]
        ),

        FailureMode.POOR_EXAMPLES: RootCauseAnalysis(
            failure_mode=failure.mode,
            root_cause="Examples are missing, too abstract, or don't match template use cases",
            impact="Users can't visualize expected output quality",
            improvement_aspects=["example_quality", "context_provision"],
            suggested_fixes=[
                "Add 3-5 diverse examples covering common scenarios",
                "Show both good and bad examples with explanations",
                "Ensure examples match current template version",
                "Use real-world examples from successful projects"
            ]
        ),

        FailureMode.VAGUE_METRICS: RootCauseAnalysis(
            failure_mode=failure.mode,
            root_cause="Success criteria use qualitative language without specific thresholds",
            impact="Can't objectively measure success; disagreement on achievement",
            improvement_aspects=["constraint_specificity", "instruction_clarity"],
            suggested_fixes=[
                "Replace qualitative goals with quantitative metrics (e.g., ≥40% activation)",
                "Specify measurement methods for each metric",
                "Add threshold values and acceptable ranges",
                "Include examples: 'Good: 4.2/5 satisfaction' vs 'Bad: improve satisfaction'"
            ]
        ),

        FailureMode.MISSING_CONSTRAINTS: RootCauseAnalysis(
            failure_mode=failure.mode,
            root_cause="Requirements lack conditional logic, boundaries, or edge case handling",
            impact="Users apply rules incorrectly in edge cases; inconsistent interpretation",
            improvement_aspects=["constraint_specificity", "instruction_clarity"],
            suggested_fixes=[
                "Add 'when', 'if', 'unless' conditions to all requirements",
                "Specify boundaries and edge cases explicitly",
                "Provide decision trees for complex conditional logic",
                "Add examples showing how constraints apply in edge cases"
            ]
        )
    }

    return root_cause_map.get(failure.mode, RootCauseAnalysis(
        failure_mode=failure.mode,
        root_cause="Unknown root cause",
        impact="Unknown impact",
        improvement_aspects=[],
        suggested_fixes=[]
    ))


# 8 improvement aspects from plan.md Phase 2
IMPROVEMENT_ASPECTS = [
    "instruction_clarity",
    "context_provision",
    "chain_of_thought",
    "tool_definitions",
    "example_quality",
    "constraint_specificity",
    "format_specification",
    "error_handling"
]
