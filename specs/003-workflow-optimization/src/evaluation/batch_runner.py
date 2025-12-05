"""
Batch Evaluation Runner and Result Storage

Orchestrates evaluation of multiple templates using the multi-judge system.

Tasks: T043-T044 (Batch runner, result storage)
"""

import json
import yaml
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import hashlib

from .judge_interface import JudgeScore, STANDARD_RUBRIC
from .reliability import compute_reliability_metrics, ReliabilityMetrics
from .consensus import aggregate_judges, AggregatedScore
from .failure_modes import FailureClassifier, FailureClassification


@dataclass
class EvaluationResult:
    """Complete evaluation result for a template (from data-model.md)"""
    id: str  # UUID
    timestamp: str  # ISO 8601
    target_path: str
    target_version: str
    content_hash: str

    # Judge scores
    judge_scores: List[Dict]  # List of JudgeScore dicts

    # Aggregated scores
    aggregated: Dict  # AggregatedScore dict

    # Reliability metrics
    reliability: Dict  # ReliabilityMetrics dict

    # Failure modes
    failures: List[Dict]  # List of FailureClassification dicts

    # Metadata
    duration_seconds: float
    total_cost_usd: float


class BatchEvaluationRunner:
    """
    Runs evaluation on multiple templates using multi-judge consensus.
    """

    def __init__(
        self,
        judges: List,  # List of JudgeInterface instances
        rubric: Optional[Dict] = None,
        output_dir: str = "evaluations"
    ):
        """
        Initialize batch runner.

        Args:
            judges: List of initialized judge instances
            rubric: Evaluation rubric (uses STANDARD_RUBRIC if None)
            output_dir: Directory to save evaluation results
        """
        self.judges = judges
        self.rubric = rubric or STANDARD_RUBRIC
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.failure_classifier = FailureClassifier()

    def evaluate_template(
        self,
        template_path: str,
        template_content: str,
        version: str = "unknown"
    ) -> EvaluationResult:
        """
        Evaluate a single template with all judges.

        Args:
            template_path: Path to template file
            template_content: Template content to evaluate
            version: Template version (e.g., "v0.0.3")

        Returns:
            EvaluationResult with all scores and analysis
        """
        start_time = datetime.now()

        # Calculate content hash
        content_hash = hashlib.sha256(template_content.encode()).hexdigest()

        # Run all judges in parallel (in production, use async/concurrent execution)
        judge_scores = []
        total_cost = 0.0

        for judge in self.judges:
            try:
                score = judge.evaluate(template_content, self.rubric)
                judge_scores.append(score)
                total_cost += score.cost_usd
            except Exception as e:
                print(f"Warning: Judge {judge.judge_id} failed: {e}")

        if not judge_scores:
            raise ValueError("No judges succeeded in evaluation")

        # Extract dimensional scores for aggregation
        dimensional_scores = {}
        for dimension in self.rubric.keys():
            dimensional_scores[dimension] = {
                score.judge_id: score.dimensions[dimension].raw_score
                for score in judge_scores
                if dimension in score.dimensions
            }

        # Extract overall scores
        overall_scores = {score.judge_id: score.overall_score for score in judge_scores}

        # Calculate reliability metrics
        judge_score_lists = {
            judge_id: [dimensional_scores[dim][judge_id] for dim in dimensional_scores]
            for judge_id in overall_scores.keys()
        }
        reliability = compute_reliability_metrics(judge_score_lists)

        # Aggregate scores using Bradley-Terry
        aggregated = aggregate_judges(overall_scores, dimensional_scores)

        # Detect failure modes
        failures = self.failure_classifier.classify_content(
            template_content,
            aggregated.dimensional_scores
        )

        # Calculate duration
        duration = (datetime.now() - start_time).total_seconds()

        # Create evaluation result
        result = EvaluationResult(
            id=self._generate_id(),
            timestamp=datetime.now().isoformat(),
            target_path=template_path,
            target_version=version,
            content_hash=content_hash,
            judge_scores=[self._judge_score_to_dict(s) for s in judge_scores],
            aggregated=asdict(aggregated),
            reliability=asdict(reliability),
            failures=[asdict(f) for f in failures],
            duration_seconds=duration,
            total_cost_usd=total_cost
        )

        return result

    def evaluate_batch(
        self,
        templates: List[Dict[str, str]],
        save_results: bool = True
    ) -> List[EvaluationResult]:
        """
        Evaluate multiple templates in batch.

        Args:
            templates: List of dicts with keys:
                      - path: Template file path
                      - content: Template content
                      - version: Template version
            save_results: Whether to save results to disk

        Returns:
            List of EvaluationResult objects
        """
        results = []

        for i, template in enumerate(templates):
            print(f"Evaluating {i+1}/{len(templates)}: {template['path']}")

            try:
                result = self.evaluate_template(
                    template['path'],
                    template['content'],
                    template.get('version', 'unknown')
                )
                results.append(result)

                if save_results:
                    self.save_result(result)

            except Exception as e:
                print(f"Error evaluating {template['path']}: {e}")

        return results

    def save_result(self, result: EvaluationResult, format: str = "yaml"):
        """
        Save evaluation result to file.

        Args:
            result: EvaluationResult to save
            format: "yaml" or "json"
        """
        # Generate filename
        timestamp = datetime.fromisoformat(result.timestamp).strftime("%Y%m%d_%H%M%S")
        template_name = Path(result.target_path).stem
        filename = f"eval_{timestamp}_{template_name}_{result.target_version}.{format}"

        filepath = self.output_dir / filename

        # Convert to dict
        result_dict = asdict(result)

        # Save
        if format == "yaml":
            with open(filepath, 'w') as f:
                yaml.dump(result_dict, f, default_flow_style=False, sort_keys=False)
        else:  # json
            with open(filepath, 'w') as f:
                json.dump(result_dict, f, indent=2)

        print(f"Saved evaluation result: {filepath}")

    def load_result(self, filepath: str) -> EvaluationResult:
        """
        Load evaluation result from file.

        Args:
            filepath: Path to saved result

        Returns:
            EvaluationResult object
        """
        filepath = Path(filepath)

        if filepath.suffix == '.yaml' or filepath.suffix == '.yml':
            with open(filepath, 'r') as f:
                data = yaml.safe_load(f)
        else:  # json
            with open(filepath, 'r') as f:
                data = json.load(f)

        return EvaluationResult(**data)

    def _generate_id(self) -> str:
        """Generate unique evaluation ID"""
        import uuid
        return str(uuid.uuid4())

    def _judge_score_to_dict(self, score: JudgeScore) -> Dict:
        """Convert JudgeScore to dictionary"""
        return {
            "judge_id": score.judge_id,
            "model_name": score.model_name,
            "role": score.role.value,
            "dimensions": {
                name: asdict(dim) for name, dim in score.dimensions.items()
            },
            "overall_score": score.overall_score,
            "reasoning": score.reasoning,
            "confidence": score.confidence,
            "evaluation_time_seconds": score.evaluation_time_seconds,
            "token_count": score.token_count,
            "cost_usd": score.cost_usd
        }


class EvaluationStorage:
    """
    Manages storage and retrieval of evaluation results.
    """

    def __init__(self, storage_dir: str = "evaluations"):
        """
        Initialize storage.

        Args:
            storage_dir: Directory for storing results
        """
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)

    def list_evaluations(
        self,
        template_path: Optional[str] = None,
        version: Optional[str] = None
    ) -> List[str]:
        """
        List stored evaluation results.

        Args:
            template_path: Filter by template path (optional)
            version: Filter by version (optional)

        Returns:
            List of evaluation file paths
        """
        pattern = "eval_*.yaml"
        files = list(self.storage_dir.glob(pattern)) + list(self.storage_dir.glob("eval_*.json"))

        # Filter by template and/or version if specified
        if template_path or version:
            filtered = []
            for f in files:
                # Parse filename: eval_TIMESTAMP_TEMPLATE_VERSION.ext
                parts = f.stem.split('_')
                if len(parts) >= 4:
                    file_template = parts[2]
                    file_version = parts[3]

                    if template_path and Path(template_path).stem != file_template:
                        continue
                    if version and version != file_version:
                        continue

                    filtered.append(str(f))
            return filtered

        return [str(f) for f in files]

    def get_latest_evaluation(self, template_path: str) -> Optional[EvaluationResult]:
        """
        Get most recent evaluation for a template.

        Args:
            template_path: Template path

        Returns:
            Latest EvaluationResult or None if not found
        """
        evals = self.list_evaluations(template_path=template_path)
        if not evals:
            return None

        # Sort by timestamp (filename contains timestamp)
        evals.sort(reverse=True)

        # Load and return latest
        runner = BatchEvaluationRunner(judges=[])  # Empty judges just for loading
        return runner.load_result(evals[0])

    def compare_evaluations(
        self,
        baseline_id: str,
        optimized_id: str
    ) -> Dict:
        """
        Compare two evaluations (for validation stage).

        Args:
            baseline_id: Evaluation ID of baseline version
            optimized_id: Evaluation ID of optimized version

        Returns:
            Comparison dict with deltas
        """
        # Find evaluation files
        baseline_file = None
        optimized_file = None

        for f in self.storage_dir.glob("eval_*.*"):
            content = f.read_text()
            if baseline_id in content:
                baseline_file = f
            if optimized_id in content:
                optimized_file = f

        if not baseline_file or not optimized_file:
            raise ValueError("Could not find evaluation files")

        # Load evaluations
        runner = BatchEvaluationRunner(judges=[])
        baseline = runner.load_result(str(baseline_file))
        optimized = runner.load_result(str(optimized_file))

        # Compare scores
        baseline_score = baseline.aggregated['overall_score']
        optimized_score = optimized.aggregated['overall_score']

        improvement = optimized_score - baseline_score
        improvement_pct = (improvement / baseline_score) * 100 if baseline_score > 0 else 0

        # Dimensional comparisons
        dim_comparisons = {}
        for dim in baseline.aggregated['dimensional_scores'].keys():
            baseline_dim = baseline.aggregated['dimensional_scores'][dim]
            optimized_dim = optimized.aggregated['dimensional_scores'][dim]
            delta = optimized_dim - baseline_dim

            dim_comparisons[dim] = {
                "baseline": baseline_dim,
                "optimized": optimized_dim,
                "delta": delta,
                "status": "improved" if delta > 0 else ("regressed" if delta < 0 else "unchanged")
            }

        return {
            "baseline_id": baseline_id,
            "optimized_id": optimized_id,
            "overall": {
                "baseline": baseline_score,
                "optimized": optimized_score,
                "improvement": improvement,
                "improvement_percentage": improvement_pct
            },
            "dimensions": dim_comparisons,
            "reliability": {
                "baseline_kappa": baseline.reliability['fleiss_kappa'],
                "optimized_kappa": optimized.reliability['fleiss_kappa']
            }
        }
