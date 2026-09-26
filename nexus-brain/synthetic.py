"""Deterministic synthetic cell-state generator.

The generator creates a controlled world for software validation. Synthetic
patterns are not intended to represent real biological distributions.
"""

from __future__ import annotations

from dataclasses import dataclass
import random


@dataclass(frozen=True, slots=True)
class SyntheticObservation:
    entity_id: str
    time_index: int
    values: tuple[float, ...]
    future_state: int


def generate_trajectory(
    *,
    entity_id: str,
    seed: int,
    steps: int = 5,
    dimensions: int = 8,
    noise: float = 0.03,
) -> list[SyntheticObservation]:
    """Generate a reproducible trajectory with a hidden future transition.

    The latent state gradually moves toward a second state. The returned
    future_state is metadata for evaluation and is never used by the
    trajectory representation itself.
    """
    if steps < 2:
        raise ValueError("steps must be at least 2")
    if dimensions < 1:
        raise ValueError("dimensions must be positive")
    if noise < 0:
        raise ValueError("noise cannot be negative")

    rng = random.Random(seed)
    observations: list[SyntheticObservation] = []

    start = [rng.uniform(0.15, 0.35) for _ in range(dimensions)]
    target = [rng.uniform(0.65, 0.90) for _ in range(dimensions)]

    for t in range(steps):
        progress = t / (steps - 1)
        values = tuple(
            max(0.0, min(1.0, start[i] + (target[i] - start[i]) * progress + rng.gauss(0, noise)))
            for i in range(dimensions)
        )
        observations.append(
            SyntheticObservation(
                entity_id=entity_id,
                time_index=t,
                values=values,
                future_state=1 if progress >= 0.75 else 0,
            )
        )

    return observations
