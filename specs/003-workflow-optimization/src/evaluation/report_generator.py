"""
Evaluation Report Generator

Creates markdown reports from evaluation results.

Tasks: T045 (Report generator)
"""

from typing import Dict, List
from pathlib import Path
from datetime import datetime

from .batch_runner import EvaluationResult
from .reliability import interpret_kappa


class ReportGenerator:
    """
    Generates human-readable markdown reports from evaluation results.
    """

    def generate_report(self, result: EvaluationResult) -> str:
        """
        Generate comprehensive markdown report from evaluation result.

        Args:
            result: EvaluationResult to report on

        Returns:
            Markdown-formatted report string
        """
        sections = [
            self._header(result),
            self._overall_assessment(result),
            self._dimensional_breakdown(result),
            self._reliability_metrics(result),
            self._failure_modes(result),
            self._judge_contributions(result),
            self._metadata(result)
        ]

        return "\n\n".join(sections)

    def _header(self, result: EvaluationResult) -> str:
        """Generate report header"""
        template_name = Path(result.target_path).name
        timestamp = datetime.fromisoformat(result.timestamp).strftime("%Y-%m-%d %H:%M:%S")

        return f"""# Evaluation Report: {template_name}

**Version**: {result.target_version}
**Evaluated**: {timestamp}
**Evaluation ID**: `{result.id}`
**Duration**: {result.duration_seconds:.1f}s
**Cost**: ${result.total_cost_usd:.4f}

---"""

    def _overall_assessment(self, result: EvaluationResult) -> str:
        """Generate overall assessment section"""
        score = result.aggregated['overall_score']
        confidence = result.aggregated['confidence']

        # Quality level
        if score >= 9.0:
            level = "Exceptional"
            emoji = "🌟"
        elif score >= 7.0:
            level = "Strong"
            emoji = "✅"
        elif score >= 5.0:
            level = "Adequate"
            emoji = "⚠️"
        else:
            level = "Needs Improvement"
            emoji = "❌"

        return f"""## Overall Assessment

{emoji} **Overall Score: {score:.1f} / 10.0** ({level} Quality)

**Consensus Confidence**: {confidence:.0%}
**Method**: {result.aggregated['method'].replace('_', ' ').title()}"""

    def _dimensional_breakdown(self, result: EvaluationResult) -> str:
        """Generate dimensional scores section"""
        dims = result.aggregated['dimensional_scores']

        # Sort by score (lowest first to highlight improvement opportunities)
        sorted_dims = sorted(dims.items(), key=lambda x: x[1])

        lines = ["## Dimensional Breakdown\n"]

        for dim_name, score in sorted_dims:
            # Get weight from rubric (assuming standard rubric structure)
            weight = self._get_dimension_weight(dim_name)

            # Status emoji
            if score >= 8.0:
                status = "✅"
            elif score >= 6.0:
                status = "⚠️"
            else:
                status = "❌"

            lines.append(
                f"{status} **{dim_name.replace('_', ' ').title()}**: {score:.1f}/10 "
                f"(weight: {weight:.0%})"
            )

        return "\n".join(lines)

    def _reliability_metrics(self, result: EvaluationResult) -> str:
        """Generate reliability metrics section"""
        reliability = result.reliability
        kappa = reliability['fleiss_kappa']
        level, interpretation = interpret_kappa(kappa)

        # Pairwise agreements
        pairwise_lines = []
        for pair, rate in reliability['pairwise_agreements'].items():
            judge_a, judge_b = pair.split('_')
            pairwise_lines.append(f"  - {judge_a} ↔ {judge_b}: {rate:.0%}")

        pairwise_text = "\n".join(pairwise_lines) if pairwise_lines else "  - N/A"

        return f"""## Reliability Metrics

**Fleiss' Kappa**: {kappa:.2f} ({level})
> {interpretation}

**Score Variance**: {reliability['variance']:.2f}
**Consensus Confidence**: {reliability['consensus_confidence']:.0%}

**Pairwise Judge Agreement**:
{pairwise_text}"""

    def _failure_modes(self, result: EvaluationResult) -> str:
        """Generate failure modes section"""
        failures = result.failures

        if not failures:
            return """## Failure Modes

✅ **No significant failure modes detected**

Template quality is high with no critical issues identified."""

        lines = ["## Failure Modes\n"]

        for i, failure in enumerate(failures, 1):
            severity_emoji = {
                "critical": "🔴",
                "moderate": "🟡",
                "minor": "🟢"
            }.get(failure['severity'], "⚪")

            lines.append(f"### {i}. {failure['mode'].replace('_', ' ').title()} {severity_emoji}\n")
            lines.append(f"**Severity**: {failure['severity'].title()}")
            lines.append(f"**Confidence**: {failure['confidence']:.0%}")
            lines.append(f"**Affected Dimensions**: {', '.join(failure['affected_dimensions'])}\n")
            lines.append(f"**Description**: {failure['description']}\n")
            lines.append(f"**Evidence**:")
            lines.append(f"```\n{failure['evidence']}\n```\n")

        return "\n".join(lines)

    def _judge_contributions(self, result: EvaluationResult) -> str:
        """Generate judge contributions section"""
        contributions = result.aggregated['judge_contributions']

        lines = ["## Judge Contributions\n"]
        lines.append("How much each judge influenced the final score:\n")

        for judge_id, weight in sorted(contributions.items(), key=lambda x: -x[1]):
            bar_length = int(weight * 20)  # Max 20 chars
            bar = "█" * bar_length
            lines.append(f"- **{judge_id}**: {weight:.0%} {bar}")

        return "\n".join(lines)

    def _metadata(self, result: EvaluationResult) -> str:
        """Generate metadata section"""
        num_judges = len(result.judge_scores)

        return f"""## Metadata

**Judges Used**: {num_judges}
**Content Hash**: `{result.content_hash[:16]}...`
**Evaluation Time**: {result.duration_seconds:.1f}s
**Total Cost**: ${result.total_cost_usd:.4f}

---

*Generated by PMF-Kit Workflow Optimization v0.0.4*"""

    def _get_dimension_weight(self, dim_name: str) -> float:
        """Get dimension weight from standard rubric"""
        from .judge_interface import STANDARD_RUBRIC
        return STANDARD_RUBRIC.get(dim_name, {}).get('weight', 0.0)

    def generate_comparison_report(self, comparison: Dict) -> str:
        """
        Generate comparison report for baseline vs. optimized.

        Args:
            comparison: Comparison dict from EvaluationStorage.compare_evaluations()

        Returns:
            Markdown-formatted comparison report
        """
        overall = comparison['overall']
        dims = comparison['dimensions']

        # Header
        report = f"""# Optimization Comparison Report

**Baseline**: `{comparison['baseline_id']}`
**Optimized**: `{comparison['optimized_id']}`
**Generated**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

## Overall Improvement

**Baseline Score**: {overall['baseline']:.2f} / 10.0
**Optimized Score**: {overall['optimized']:.2f} / 10.0

**Improvement**: {overall['improvement']:+.2f} points ({overall['improvement_percentage']:+.1f}%)

"""

        # Improvement status
        if overall['improvement'] >= 0.5:
            report += "✅ **Significant Improvement Achieved**\n\n"
        elif overall['improvement'] >= 0.1:
            report += "✓ **Moderate Improvement Achieved**\n\n"
        elif overall['improvement'] > -0.1:
            report += "→ **Minimal Change**\n\n"
        else:
            report += "❌ **Regression Detected**\n\n"

        # Dimensional changes
        report += "## Dimensional Changes\n\n"

        # Separate improvements and regressions
        improvements = []
        regressions = []
        unchanged = []

        for dim, data in sorted(dims.items(), key=lambda x: -x[1]['delta']):
            if data['status'] == 'improved':
                improvements.append((dim, data))
            elif data['status'] == 'regressed':
                regressions.append((dim, data))
            else:
                unchanged.append((dim, data))

        if improvements:
            report += "### Improvements 📈\n\n"
            for dim, data in improvements:
                report += (
                    f"- **{dim.replace('_', ' ').title()}**: "
                    f"{data['baseline']:.1f} → {data['optimized']:.1f} "
                    f"({data['delta']:+.1f})\n"
                )
            report += "\n"

        if regressions:
            report += "### Regressions 📉\n\n"
            for dim, data in regressions:
                report += (
                    f"- **{dim.replace('_', ' ').title()}**: "
                    f"{data['baseline']:.1f} → {data['optimized']:.1f} "
                    f"({data['delta']:+.1f})\n"
                )
            report += "\n"

        # Reliability comparison
        reliability = comparison['reliability']
        report += f"""## Reliability Comparison

**Baseline Fleiss' Kappa**: {reliability['baseline_kappa']:.2f}
**Optimized Fleiss' Kappa**: {reliability['optimized_kappa']:.2f}

---

*Generated by PMF-Kit Workflow Optimization v0.0.4*
"""

        return report

    def save_report(self, report: str, output_path: str):
        """
        Save report to file.

        Args:
            report: Markdown report string
            output_path: File path to save to
        """
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w') as f:
            f.write(report)

        print(f"Report saved: {output_file}")
