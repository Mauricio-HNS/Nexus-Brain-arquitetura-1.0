"""Trajectory primitives for the Nexus research hypothesis.

This module contains intentionally transparent mathematics. It does not
perform clinical prediction or biological diagnosis.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Sequence


@dataclass(frozen=True, slots=True)
class TrajectoryPoint:
    """One time-indexed research observation."""

    time_index: int
    values: tuple[float, ...]


@dataclass(frozen=True, slots=True)
class TrajectorySummary:
    """Deterministic summary of how an observation sequence changes."""

    displacement: float
    velocity: float
    acceleration: float


def _distance(a: Sequence[float], b: Sequence[float]) -> float:
    if len(a) != len(b):
        raise ValueError("trajectory points must have equal dimensionality")
    return sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def summarize_trajectory(points: Sequence[TrajectoryPoint]) -> TrajectorySummary:
    """Summarize state change using consecutive Euclidean distances.

    The function is a research baseline, not a biological model.
    """
    if len(points) < 2:
        raise ValueError("at least two trajectory points are required")

    ordered = sorted(points, key=lambda point: point.time_index)
    distances = [
        _distance(current.values, previous.values)
        for previous, current in zip(ordered, ordered[1:])
    ]

    displacement = _distance(ordered[0].values, ordered[-1].values)
    velocity = sum(distances) / len(distances)

    if len(distances) < 2:
        acceleration = 0.0
    else:
        acceleration = sum(
            distances[index] - distances[index - 1]
            for index in range(1, len(distances))
        ) / (len(distances) - 1)

    return TrajectorySummary(
        displacement=displacement,
        velocity=velocity,
        acceleration=acceleration,
    )
