"""
Reliability Metrics for Multi-Judge Evaluation

Implements inter-rater reliability measures to assess agreement between LLM judges.

Tasks: T030 (Fleiss' kappa calculation)
"""

import numpy as np
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class ReliabilityMetrics:
    """Inter-judge agreement metrics"""
    fleiss_kappa: float  # Overall agreement (-1.0 to 1.0)
    pairwise_agreements: Dict[str, float]  # Judge-to-judge agreement rates
    variance: float  # Score variance across judges
    consensus_confidence: float  # 0.0-1.0


def calculate_fleiss_kappa(ratings: np.ndarray) -> float:
    """
    Calculate Fleiss' kappa for inter-rater reliability.

    Fleiss' kappa measures agreement between multiple raters who assign
    categorical ratings to items. Values:
    - < 0.0: Poor agreement (worse than chance)
    - 0.0-0.20: Slight agreement
    - 0.21-0.40: Fair agreement
    - 0.41-0.60: Moderate agreement (TARGET for PMF-Kit)
    - 0.61-0.80: Substantial agreement
    - 0.81-1.00: Almost perfect agreement

    Args:
        ratings: 2D array of shape (n_items, n_raters)
                 Each row is an item, each column is a rater
                 Values are categorical ratings (e.g., 1-10 scores)

    Returns:
        Fleiss' kappa coefficient (-1.0 to 1.0)

    Reference:
        Fleiss, J. L. (1971). "Measuring nominal scale agreement among many raters."
        Psychological Bulletin, 76(5), 378-382.
    """
    n_items, n_raters = ratings.shape

    # Convert continuous scores to categories (bins)
    # For 0-10 scale, use 5 categories: Poor (0-2), Weak (3-4), Adequate (5-6), Strong (7-8), Exceptional (9-10)
    categories = np.digitize(ratings, bins=[0, 2.5, 4.5, 6.5, 8.5, 10.5]) - 1
    n_categories = 5

    # Count how many raters assigned each category to each item
    category_counts = np.zeros((n_items, n_categories))
    for i in range(n_items):
        for c in range(n_categories):
            category_counts[i, c] = np.sum(categories[i, :] == c)

    # Calculate p_i for each item (proportion of all possible rater pairs that agreed)
    p_i = np.zeros(n_items)
    for i in range(n_items):
        sum_n_ij_squared = np.sum(category_counts[i, :] ** 2)
        p_i[i] = (sum_n_ij_squared - n_raters) / (n_raters * (n_raters - 1))

    # Mean agreement across all items
    P_bar = np.mean(p_i)

    # Calculate p_j (proportion of all assignments in category j)
    p_j = np.sum(category_counts, axis=0) / (n_items * n_raters)

    # Expected agreement by chance
    P_e_bar = np.sum(p_j ** 2)

    # Fleiss' kappa
    if P_e_bar == 1.0:
        return 1.0  # Perfect agreement
    kappa = (P_bar - P_e_bar) / (1 - P_e_bar)

    return float(kappa)


def calculate_pairwise_agreement(
    judge_scores: Dict[str, List[float]],
    tolerance: float = 1.0
) -> Dict[str, float]:
    """
    Calculate pairwise agreement rates between judges.

    Agreement is defined as: |score_A - score_B| <= tolerance

    Args:
        judge_scores: Dict mapping judge_id to list of scores
                     e.g., {"gpt4o": [8.5, 7.2, ...], "claude": [8.3, 7.5, ...]}
        tolerance: Maximum difference to consider as "agreement" (default: 1.0 point)

    Returns:
        Dict mapping judge pairs to agreement rate (0.0-1.0)
        e.g., {"gpt4o_claude": 0.85, "gpt4o_gemini": 0.72, ...}
    """
    judge_ids = list(judge_scores.keys())
    pairwise = {}

    for i in range(len(judge_ids)):
        for j in range(i + 1, len(judge_ids)):
            judge_a = judge_ids[i]
            judge_b = judge_ids[j]

            scores_a = np.array(judge_scores[judge_a])
            scores_b = np.array(judge_scores[judge_b])

            # Calculate agreement rate
            differences = np.abs(scores_a - scores_b)
            agreements = np.sum(differences <= tolerance)
            agreement_rate = agreements / len(scores_a)

            pair_key = f"{judge_a}_{judge_b}"
            pairwise[pair_key] = float(agreement_rate)

    return pairwise


def calculate_score_variance(judge_scores: Dict[str, List[float]]) -> float:
    """
    Calculate variance in scores across judges.

    High variance indicates judges have divergent opinions.
    Low variance indicates judges are more consistent.

    Args:
        judge_scores: Dict mapping judge_id to list of scores

    Returns:
        Variance value
    """
    all_scores = []
    for scores in judge_scores.values():
        all_scores.extend(scores)

    return float(np.var(all_scores))


def calculate_consensus_confidence(
    fleiss_kappa: float,
    variance: float,
    n_judges: int
) -> float:
    """
    Calculate overall confidence in multi-judge consensus.

    Combines multiple reliability indicators into single confidence score.

    Args:
        fleiss_kappa: Fleiss' kappa value
        variance: Score variance
        n_judges: Number of judges

    Returns:
        Confidence score (0.0-1.0)
    """
    # Normalize kappa to 0-1 range (kappa can be negative)
    kappa_normalized = max(0.0, fleiss_kappa)

    # Variance penalty (high variance reduces confidence)
    # Assuming 0-10 scale, variance typically 0-4
    variance_factor = 1.0 - min(variance / 4.0, 1.0)

    # Judge count bonus (more judges = more confidence)
    # Diminishing returns after 5 judges
    judge_factor = min(n_judges / 5.0, 1.0)

    # Weighted combination
    confidence = (
        0.5 * kappa_normalized +
        0.3 * variance_factor +
        0.2 * judge_factor
    )

    return float(np.clip(confidence, 0.0, 1.0))


def compute_reliability_metrics(
    judge_scores: Dict[str, List[float]],
    tolerance: float = 1.0
) -> ReliabilityMetrics:
    """
    Compute complete reliability metrics for multi-judge evaluation.

    Args:
        judge_scores: Dict mapping judge_id to list of scores
        tolerance: Agreement tolerance for pairwise metrics

    Returns:
        ReliabilityMetrics object with all metrics

    Example:
        >>> scores = {
        ...     "gpt4o": [8.5, 7.2, 9.1, 6.8],
        ...     "claude": [8.3, 7.5, 9.0, 7.1],
        ...     "gemini": [8.7, 7.0, 8.9, 6.5]
        ... }
        >>> metrics = compute_reliability_metrics(scores)
        >>> print(f"Kappa: {metrics.fleiss_kappa:.2f}")
        Kappa: 0.52
    """
    # Convert to numpy array for Fleiss' kappa
    judge_ids = sorted(judge_scores.keys())
    n_items = len(judge_scores[judge_ids[0]])
    n_judges = len(judge_ids)

    ratings = np.zeros((n_items, n_judges))
    for j, judge_id in enumerate(judge_ids):
        ratings[:, j] = judge_scores[judge_id]

    # Calculate metrics
    fleiss_kappa = calculate_fleiss_kappa(ratings)
    pairwise = calculate_pairwise_agreement(judge_scores, tolerance)
    variance = calculate_score_variance(judge_scores)
    confidence = calculate_consensus_confidence(fleiss_kappa, variance, n_judges)

    return ReliabilityMetrics(
        fleiss_kappa=fleiss_kappa,
        pairwise_agreements=pairwise,
        variance=variance,
        consensus_confidence=confidence
    )


def interpret_kappa(kappa: float) -> Tuple[str, str]:
    """
    Interpret Fleiss' kappa value with qualitative description.

    Args:
        kappa: Fleiss' kappa value

    Returns:
        Tuple of (level, interpretation)
    """
    if kappa < 0.0:
        return ("Poor", "Agreement worse than chance")
    elif kappa < 0.21:
        return ("Slight", "Minimal agreement between judges")
    elif kappa < 0.41:
        return ("Fair", "Weak agreement; consider adding judges or refining rubric")
    elif kappa < 0.61:
        return ("Moderate", "Acceptable agreement for evaluation")
    elif kappa < 0.81:
        return ("Substantial", "Strong agreement between judges")
    else:
        return ("Almost Perfect", "Exceptional agreement")


# Acceptance thresholds for PMF-Kit optimization
KAPPA_THRESHOLD_GO = 0.40  # Minimum for production use (Phase 0 exit criteria)
KAPPA_THRESHOLD_IDEAL = 0.60  # Target for high-confidence evaluation
VARIANCE_THRESHOLD_HIGH = 3.0  # High variance warning (0-10 scale)
PAIRWISE_THRESHOLD_LOW = 0.65  # Low pairwise agreement warning
