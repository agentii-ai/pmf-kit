"""
Judge Interface for PMF-Kit Template Evaluation

This module defines the abstract base class for LLM judges that evaluate
PMF-Kit templates using the G-Eval chain-of-thought methodology.

Tasks: T025 (Judge Interface)
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum


class JudgeRole(Enum):
    """Judge evaluation stance"""
    STRICT = "strict"  # High standards, critical lens
    BALANCED = "balanced"  # Practical, fair assessment
    LENIENT = "lenient"  # Supportive, encouraging lens


@dataclass
class DimensionalScore:
    """Score for a single evaluation dimension"""
    dimension: str
    raw_score: float  # 0.0-10.0
    weight: float  # 0.0-1.0
    weighted_score: float  # raw_score * weight
    evidence: str  # Supporting quotes/examples
    reasoning: str  # Chain-of-thought explanation
    confidence: float  # 0.0-1.0


@dataclass
class JudgeScore:
    """Complete evaluation result from a single judge"""
    judge_id: str
    model_name: str
    role: JudgeRole

    # Dimensional scores
    dimensions: Dict[str, DimensionalScore]

    # Overall assessment
    overall_score: float  # Weighted sum of dimensional scores
    reasoning: str  # Overall chain-of-thought
    confidence: float  # 0.0-1.0

    # Metadata
    evaluation_time_seconds: float
    token_count: int
    cost_usd: float


class JudgeInterface(ABC):
    """
    Abstract base class for LLM judges.

    Implements the G-Eval methodology:
    1. Load template content
    2. Apply chain-of-thought reasoning
    3. Score each dimension with evidence
    4. Aggregate to overall score
    """

    def __init__(self, judge_id: str, model_name: str, role: JudgeRole, api_key: Optional[str] = None):
        """
        Initialize judge.

        Args:
            judge_id: Unique identifier (e.g., "gpt4o", "claude35sonnet")
            model_name: Full model name for API calls
            role: Evaluation stance (strict/balanced/lenient)
            api_key: Optional API key (uses env var if not provided)
        """
        self.judge_id = judge_id
        self.model_name = model_name
        self.role = role
        self.api_key = api_key

    @abstractmethod
    def evaluate(self, template_content: str, rubric: Dict[str, any]) -> JudgeScore:
        """
        Evaluate template using G-Eval chain-of-thought methodology.

        Args:
            template_content: The template/spec/plan content to evaluate
            rubric: Evaluation rubric with dimensions and weights

        Returns:
            JudgeScore with dimensional and overall scores

        Raises:
            JudgeEvaluationError: If evaluation fails (API error, parsing error, etc.)
        """
        pass

    @abstractmethod
    def _format_prompt(self, template_content: str, rubric: Dict[str, any]) -> str:
        """
        Format the evaluation prompt for this specific judge/model.

        Different models may have different prompt structures (e.g., Claude uses
        XML tags, OpenAI prefers markdown, etc.)

        Args:
            template_content: Content to evaluate
            rubric: Evaluation rubric

        Returns:
            Formatted prompt string
        """
        pass

    @abstractmethod
    def _parse_response(self, response: str) -> Dict[str, DimensionalScore]:
        """
        Parse judge's response into structured dimensional scores.

        Args:
            response: Raw text response from LLM

        Returns:
            Dictionary mapping dimension names to DimensionalScore objects

        Raises:
            ResponseParsingError: If response format is invalid
        """
        pass

    def _calculate_overall_score(self, dimensions: Dict[str, DimensionalScore]) -> float:
        """
        Calculate weighted overall score from dimensional scores.

        Args:
            dimensions: Dictionary of dimensional scores

        Returns:
            Overall score (0.0-10.0)
        """
        return sum(dim.weighted_score for dim in dimensions.values())

    def get_role_instructions(self) -> str:
        """
        Get evaluation instructions based on judge role.

        Returns:
            Role-specific instructions to prepend to prompts
        """
        if self.role == JudgeRole.STRICT:
            return """You are a rigorous evaluator with high standards. Be critical and identify even minor issues.
Only award exceptional scores (9-10) when content truly exceeds expectations."""

        elif self.role == JudgeRole.BALANCED:
            return """You are a fair, practical evaluator. Assess content objectively, recognizing both strengths
and areas for improvement. Your scores should reflect realistic quality expectations."""

        else:  # LENIENT
            return """You are a supportive evaluator who recognizes effort and potential. While identifying areas
for improvement, emphasize what works well. Give credit for good attempts and partial successes."""


class JudgeEvaluationError(Exception):
    """Raised when judge evaluation fails"""
    pass


class ResponseParsingError(Exception):
    """Raised when judge response cannot be parsed"""
    pass


# Standard rubric dimensions and weights (from evaluation-rubric.md)
STANDARD_RUBRIC = {
    "correctness": {"weight": 0.25, "description": "Accuracy and logical validity"},
    "coherence": {"weight": 0.15, "description": "Logical flow and organization"},
    "instruction_following": {"weight": 0.15, "description": "Adherence to requirements"},
    "completeness": {"weight": 0.12, "description": "Coverage and thoroughness"},
    "specificity": {"weight": 0.10, "description": "Concreteness and actionability"},
    "clarity": {"weight": 0.10, "description": "Readability and ease of understanding"},
    "actionability": {"weight": 0.08, "description": "Ease of translating to actions"},
    "policy_adherence": {"weight": 0.05, "description": "Compliance with PMF-Kit principles"}
}


def load_rubric(rubric_path: Optional[str] = None) -> Dict[str, any]:
    """
    Load evaluation rubric from file or return standard rubric.

    Args:
        rubric_path: Optional path to custom rubric YAML file

    Returns:
        Rubric dictionary
    """
    if rubric_path:
        import yaml
        with open(rubric_path, 'r') as f:
            return yaml.safe_load(f)
    return STANDARD_RUBRIC
