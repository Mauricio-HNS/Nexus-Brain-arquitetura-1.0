# Nexus Brain Research Roadmap

## Stage 0 — Synthetic world

Goal: validate the architecture without biological claims.

- Generate synthetic Cell Signatures.
- Create normal, unknown, perturbed, and simulated target populations.
- Test multimodal fusion.
- Measure calibration, precision/recall, false positives, false negatives.

## Stage 1 — Curated research datasets

Goal: evaluate whether the same architecture can learn useful patterns from published/authorized datasets.

- Define inclusion criteria.
- Normalize metadata.
- Separate training/validation/test populations.
- Prevent patient leakage between splits.
- Record dataset licenses and provenance.

## Stage 2 — Laboratory observations

Goal: connect validated measurements without making treatment claims.

- Define instrument adapters.
- Preserve raw measurements.
- Validate repeatability.
- Compare model outputs against expert annotations.

## Stage 3 — Multimodal longitudinal research

Goal: study whether combining modalities and time improves detection of meaningful cellular changes.

- Baseline modeling.
- Temporal trajectories.
- Distribution shift detection.
- Uncertainty and abstention.

## Stage 4 — Extracorporeal systems research

Only after the computational and laboratory evidence supports further research should the project investigate integration with microfluidic/extracorporeal platforms.

No clinical use is implied by this roadmap.
