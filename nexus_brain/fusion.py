"""Simple research baseline for multimodal evidence fusion.

This is intentionally model-agnostic. It provides a deterministic baseline
that future ML models can replace and benchmark against.
"""

from collections.abc import Mapping


def fuse_modalities(scores: Mapping[str, float]) -> dict[str, float]:
    """Normalize modality scores and return a transparent aggregate.

    Missing modalities are ignored. A real model should be benchmarked against
    this baseline and should preserve modality-level attribution.
    """
    if not scores:
        return {"aggregate": 0.0, "coverage": 0.0}

    values = []
    for name, value in scores.items():
        if not 0 <= value <= 1:
            raise ValueError(f"{name} must be between 0 and 1")
        values.append(value)

    return {
        "aggregate": sum(values) / len(values),
        "coverage": len(values) / 8,
    }
