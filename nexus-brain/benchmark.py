"""Transparent benchmark for the Nexus trajectory hypothesis.

Compares a current-snapshot heuristic with a trajectory heuristic on the
synthetic world. This is a software experiment, not a biological model.
"""

from dataclasses import dataclass
from statistics import mean
from .synthetic import generate_trajectory

@dataclass(frozen=True, slots=True)
class BenchmarkResult:
    seed: int
    snapshot_score: float
    trajectory_score: float
    trajectory_gain: float

def _distance_to_target(values: tuple[float, ...], target: float) -> float:
    return mean(abs(value - target) for value in values)

def run_benchmark(*, seeds: range = range(20), steps: int = 5, noise: float = 0.03) -> list[BenchmarkResult]:
    """Run a transparent synthetic comparison with the final observation held out."""
    results = []
    for seed in seeds:
        observations = generate_trajectory(entity_id=f"synthetic-{seed}", seed=seed, steps=steps, dimensions=8, noise=noise)
        history = observations[:-1]
        latest = history[-1].values
        snapshot_score = 1.0 - _distance_to_target(latest, 0.75)
        previous = history[-2].values
        delta = mean(current - old for current, old in zip(latest, previous))
        trajectory_score = max(0.0, min(1.0, snapshot_score + max(delta, 0.0)))
        results.append(BenchmarkResult(seed, snapshot_score, trajectory_score, trajectory_score - snapshot_score))
    return results

def summarize(results: list[BenchmarkResult]) -> dict[str, float]:
    if not results:
        raise ValueError("at least one benchmark result is required")
    return {
        "seeds": float(len(results)),
        "mean_snapshot_score": mean(r.snapshot_score for r in results),
        "mean_trajectory_score": mean(r.trajectory_score for r in results),
        "mean_trajectory_gain": mean(r.trajectory_gain for r in results),
    }
