"""
Multi-Judge Consensus Aggregation

Implements Bradley-Terry model for aggregating scores from multiple judges.
More stable than Elo ratings for pairwise comparisons.

Tasks: T032 (Multi-judge consensus aggregation)
"""

import numpy as np
from typing import Dict, List, Tuple
from dataclasses import dataclass
from scipy.optimize import minimize
from scipy.special import expit  # Logistic sigmoid function


@dataclass
class AggregatedScore:
    """Aggregated score from multiple judges"""
    method: str  # "bradley_terry" | "simple_average" | "weighted_average"
    overall_score: float  # Final aggregated score (0.0-10.0)
    dimensional_scores: Dict[str, float]  # Per-dimension aggregated scores
    judge_contributions: Dict[str, float]  # How much each judge influenced result
    confidence: float  # Confidence in aggregation (0.0-1.0)


def simple_average(scores: List[float]) -> float:
    """
    Simple arithmetic mean of judge scores.

    Args:
        scores: List of scores from different judges

    Returns:
        Average score
    """
    return float(np.mean(scores))


def weighted_average(scores: List[float], weights: List[float]) -> float:
    """
    Weighted average based on judge confidence/reliability.

    Args:
        scores: List of scores from different judges
        weights: Corresponding weights (typically judge confidence or historical accuracy)

    Returns:
        Weighted average score
    """
    scores_arr = np.array(scores)
    weights_arr = np.array(weights)
    weights_normalized = weights_arr / np.sum(weights_arr)

    return float(np.sum(scores_arr * weights_normalized))


def bradley_terry_aggregate(
    pairwise_comparisons: List[Tuple[int, int, float]],
    n_judges: int,
    convergence_threshold: float = 1e-6,
    max_iterations: int = 100
) -> np.ndarray:
    """
    Aggregate scores using Bradley-Terry model.

    The Bradley-Terry model estimates judge "strengths" (reliability) from
    pairwise comparisons. More reliable judges have higher influence.

    Reference:
        Bradley, R. A., & Terry, M. E. (1952). "Rank analysis of incomplete
        block designs: I. The method of paired comparisons."
        Biometrika, 39(3/4), 324-345.

    Args:
        pairwise_comparisons: List of (judge_i, judge_j, outcome) tuples
                             outcome > 0.5 means judge_i scored higher
        n_judges: Number of judges
        convergence_threshold: Stop when strength changes < threshold
        max_iterations: Maximum optimization iterations

    Returns:
        Array of judge strengths (higher = more reliable/consistent)
    """
    # Initialize judge strengths (all equal initially)
    strengths = np.ones(n_judges)

    for iteration in range(max_iterations):
        old_strengths = strengths.copy()

        # Update each judge's strength based on comparisons
        for i in range(n_judges):
            wins = 0.0
            total_comparisons = 0.0

            for j1, j2, outcome in pairwise_comparisons:
                if j1 == i:
                    wins += outcome
                    total_comparisons += 1
                elif j2 == i:
                    wins += (1 - outcome)
                    total_comparisons += 1

            if total_comparisons > 0:
                # Update strength based on win rate
                expected_wins = sum(
                    strengths[i] / (strengths[i] + strengths[j])
                    for j1, j2, _ in pairwise_comparisons
                    if (j1 == i and j2 != i) or (j2 == i and j1 != i)
                    for j in ([j2] if j1 == i else [j1])
                )
                if expected_wins > 0:
                    strengths[i] = wins / expected_wins * strengths[i]

        # Normalize strengths to sum to n_judges (maintain scale)
        strengths = strengths / np.sum(strengths) * n_judges

        # Check convergence
        if np.max(np.abs(strengths - old_strengths)) < convergence_threshold:
            break

    return strengths


def create_pairwise_comparisons(
    judge_scores: Dict[str, float],
    judge_ids: List[str]
) -> List[Tuple[int, int, float]]:
    """
    Create pairwise comparisons from judge scores.

    Args:
        judge_scores: Dict mapping judge_id to score
        judge_ids: Ordered list of judge IDs (defines indices)

    Returns:
        List of (judge_i_idx, judge_j_idx, outcome) tuples
        outcome = probability judge_i is "better" (scored higher)
    """
    comparisons = []

    for i in range(len(judge_ids)):
        for j in range(i + 1, len(judge_ids)):
            judge_i = judge_ids[i]
            judge_j = judge_ids[j]

            score_i = judge_scores[judge_i]
            score_j = judge_scores[judge_j]

            # Logistic function: convert score difference to probability
            # If scores are equal, outcome = 0.5 (tie)
            # If score_i much higher than score_j, outcome → 1.0
            score_diff = score_i - score_j
            outcome = expit(score_diff / 2.0)  # Scale factor of 2.0 for 0-10 scale

            comparisons.append((i, j, outcome))

    return comparisons


def aggregate_judges_bradley_terry(
    judge_scores: Dict[str, float],
    dimensional_scores: Dict[str, Dict[str, float]]
) -> AggregatedScore:
    """
    Aggregate multi-judge scores using Bradley-Terry model.

    Args:
        judge_scores: Dict mapping judge_id to overall score
        dimensional_scores: Dict mapping dimension to dict of judge scores
                           e.g., {"correctness": {"gpt4o": 8.5, "claude": 8.3, ...}}

    Returns:
        AggregatedScore with Bradley-Terry weighted consensus

    Example:
        >>> judge_scores = {"gpt4o": 8.5, "claude": 8.3, "gemini": 8.7}
        >>> dim_scores = {
        ...     "correctness": {"gpt4o": 8.5, "claude": 8.3, "gemini": 8.7},
        ...     "coherence": {"gpt4o": 8.0, "claude": 8.2, "gemini": 7.9}
        ... }
        >>> result = aggregate_judges_bradley_terry(judge_scores, dim_scores)
        >>> print(f"Aggregated: {result.overall_score:.2f}")
        Aggregated: 8.52
    """
    judge_ids = sorted(judge_scores.keys())
    n_judges = len(judge_ids)

    # Create pairwise comparisons from overall scores
    comparisons = create_pairwise_comparisons(judge_scores, judge_ids)

    # Estimate judge strengths (reliability weights)
    strengths = bradley_terry_aggregate(comparisons, n_judges)

    # Normalize strengths to weights (sum to 1.0)
    weights = strengths / np.sum(strengths)

    # Aggregate overall score
    overall_scores = [judge_scores[jid] for jid in judge_ids]
    overall_aggregated = weighted_average(overall_scores, weights.tolist())

    # Aggregate dimensional scores
    dim_aggregated = {}
    for dimension, dim_judge_scores in dimensional_scores.items():
        dim_scores_list = [dim_judge_scores[jid] for jid in judge_ids]
        dim_aggregated[dimension] = weighted_average(dim_scores_list, weights.tolist())

    # Calculate judge contributions
    judge_contributions = {jid: float(w) for jid, w in zip(judge_ids, weights)}

    # Confidence based on weight distribution (high entropy = low confidence)
    # If all judges weighted equally, confidence is lower
    # If one judge dominates, confidence depends on that judge's reliability
    entropy = -np.sum(weights * np.log(weights + 1e-10))
    max_entropy = np.log(n_judges)
    confidence = 1.0 - (entropy / max_entropy)

    return AggregatedScore(
        method="bradley_terry",
        overall_score=float(overall_aggregated),
        dimensional_scores=dim_aggregated,
        judge_contributions=judge_contributions,
        confidence=float(confidence)
    )


def aggregate_judges_simple(
    judge_scores: Dict[str, float],
    dimensional_scores: Dict[str, Dict[str, float]]
) -> AggregatedScore:
    """
    Aggregate multi-judge scores using simple averaging.

    Simpler fallback method when Bradley-Terry is unnecessary or fails.

    Args:
        judge_scores: Dict mapping judge_id to overall score
        dimensional_scores: Dict mapping dimension to dict of judge scores

    Returns:
        AggregatedScore with simple average
    """
    judge_ids = sorted(judge_scores.keys())
    n_judges = len(judge_ids)

    # Simple average of overall scores
    overall_scores = [judge_scores[jid] for jid in judge_ids]
    overall_aggregated = simple_average(overall_scores)

    # Simple average of dimensional scores
    dim_aggregated = {}
    for dimension, dim_judge_scores in dimensional_scores.items():
        dim_scores_list = [dim_judge_scores[jid] for jid in judge_ids]
        dim_aggregated[dimension] = simple_average(dim_scores_list)

    # Equal contributions
    judge_contributions = {jid: 1.0 / n_judges for jid in judge_ids}

    # Confidence based on variance (low variance = high confidence)
    variance = np.var(overall_scores)
    confidence = 1.0 - min(variance / 4.0, 1.0)  # Assuming 0-10 scale

    return AggregatedScore(
        method="simple_average",
        overall_score=float(overall_aggregated),
        dimensional_scores=dim_aggregated,
        judge_contributions=judge_contributions,
        confidence=float(confidence)
    )


def aggregate_judges(
    judge_scores: Dict[str, float],
    dimensional_scores: Dict[str, Dict[str, float]],
    method: str = "bradley_terry"
) -> AggregatedScore:
    """
    Aggregate scores from multiple judges using specified method.

    Args:
        judge_scores: Dict mapping judge_id to overall score
        dimensional_scores: Dict mapping dimension to dict of judge scores
        method: "bradley_terry" | "simple_average"

    Returns:
        AggregatedScore object

    Raises:
        ValueError: If method is invalid
    """
    if method == "bradley_terry":
        return aggregate_judges_bradley_terry(judge_scores, dimensional_scores)
    elif method == "simple_average":
        return aggregate_judges_simple(judge_scores, dimensional_scores)
    else:
        raise ValueError(f"Unknown aggregation method: {method}")
