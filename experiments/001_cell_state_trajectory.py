"""Experiment 001 — Cell State Trajectory.

Run:
    python experiments/001_cell_state_trajectory.py

This is a software-validation experiment. It does not model real biology.
"""

from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nexus_brain.synthetic import generate_trajectory
from nexus_brain.trajectory import TrajectoryPoint, summarize_trajectory


def run(seed: int = 42) -> dict[str, float | int]:
    observations = generate_trajectory(
        entity_id="synthetic-001",
        seed=seed,
        steps=5,
        dimensions=8,
        noise=0.03,
    )

    snapshot = observations[-2].values
    future = observations[-1].future_state

    trajectory_points = [
        TrajectoryPoint(time_index=item.time_index, values=item.values)
        for item in observations[:-1]
    ]
    summary = summarize_trajectory(trajectory_points)

    # The experiment deliberately exposes the trajectory statistics rather
    # than pretending that a medical classifier already exists.
    return {
        "seed": seed,
        "observations": len(observations),
        "snapshot_dimension": len(snapshot),
        "held_out_future_state": future,
        "trajectory_displacement": round(summary.displacement, 6),
        "trajectory_velocity": round(summary.velocity, 6),
        "trajectory_acceleration": round(summary.acceleration, 6),
    }


if __name__ == "__main__":
    result = run()
    print("NEXUS EXPERIMENT 001 — CELL STATE TRAJECTORY")
    for key, value in result.items():
        print(f"{key}: {value}")
