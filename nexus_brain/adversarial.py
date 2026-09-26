"""Experiment 003 — adversarial controls for the trajectory hypothesis.

The purpose is to stress-test the claimed temporal advantage rather than
produce a favorable demonstration. Synthetic worlds are deliberately simple
and are not biological models.
"""

from __future__ import annotations

from dataclasses import dataclass
from statistics import mean
import random

from .synthetic import generate_trajectory


@dataclass(frozen=True, slots=True)
class AdversarialResult:
    condition: str
    seed: int
    snapshot_score: float
    trajectory_score: float
    gain: float


def _score(values: tuple[float, ...], target: float = 0.75) -> float:
    return 1.0 - mean(abs(value - target) for value in values)


def _trajectory_score(history: list[tuple[float, ...]]) -> float:
    latest = history[-1]
    base = _score(latest)
    if len(history) < 2:
        return base
    delta = mean(
        current - previous
        for current, previous in zip(history[-1], history[-2])
    )
    return max(0.0, min(1.0, base + max(delta, 0.0)))


def _corrupt(
    values: tuple[float, ...],
    rng: random.Random,
    *,
    noise: float,
    missing_rate: float,
) -> tuple[float, ...]:
    result = []
    for value in values:
        if rng.random() < missing_rate:
            result.append(0.5)
        else:
            result.append(max(0.0, min(1.0, value + rng.gauss(0, noise))))
    return tuple(result)


def run_adversarial(
    *,
    seeds: range = range(50),
    steps: int = 5,
    noise: float = 0.03,
    missing_rate: float = 0.0,
) -> list[AdversarialResult]:
    """Run ordered, shuffled, noisy, and null-world controls."""
    results: list[AdversarialResult] = []

    for seed in seeds:
        observations = generate_trajectory(
            entity_id=f"synthetic-{seed}",
            seed=seed,
            steps=steps,
            dimensions=8,
            noise=noise,
        )
        rng = random.Random(seed + 10_000)

        history = [
            _corrupt(o.values, rng, noise=0.0, missing_rate=missing_rate)
            for o in observations[:-1]
        ]
        snapshot = _score(history[-1])
        trajectory = _trajectory_score(history)
        results.append(
            AdversarialResult(
                "ordered",
                seed,
                snapshot,
                trajectory,
                trajectory - snapshot,
            )
        )

        shuffled = history[:]
        rng.shuffle(shuffled)
        snapshot_shuffled = _score(shuffled[-1])
        trajectory_shuffled = _trajectory_score(shuffled)
        results.append(
            AdversarialResult(
                "shuffled_time",
                seed,
                snapshot_shuffled,
                trajectory_shuffled,
                trajectory_shuffled - snapshot_shuffled,
            )
        )

        null_history = [
            tuple(rng.uniform(0.15, 0.90) for _ in range(8))
            for _ in range(steps - 1)
        ]
        null_snapshot = _score(null_history[-1])
        null_trajectory = _trajectory_score(null_history)
        results.append(
            AdversarialResult(
                "null_world",
                seed,
                null_snapshot,
                null_trajectory,
                null_trajectory - null_snapshot,
            )
        )

    return results


def summarize_adversarial(
    results: list[AdversarialResult],
) -> dict[str, dict[str, float]]:
    if not results:
        raise ValueError("at least one adversarial result is required")

    grouped: dict[str, list[AdversarialResult]] = {}
    for result in results:
        grouped.setdefault(result.condition, []).append(result)

    return {
        condition: {
            "seeds": float(len(items)),
            "mean_snapshot_score": mean(item.snapshot_score for item in items),
            "mean_trajectory_score": mean(item.trajectory_score for item in items),
            "mean_gain": mean(item.gain for item in items),
        }
        for condition, items in grouped.items()
    }
