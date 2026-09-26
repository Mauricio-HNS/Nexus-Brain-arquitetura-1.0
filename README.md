# Nexus Brain

## Temporal Cell-State Intelligence

Nexus Brain is a research codebase for one falsifiable question:

> Can the temporal trajectory of a multimodal cellular state contain predictive information that is not present in the current snapshot alone?

The project is intentionally built from the scientific hypothesis outward. It does not begin with a medical device, a diagnostic claim, or a treatment system.

## Core idea

A snapshot describes a state at one moment.

A trajectory describes how that state changes:

```
S(t0) → S(t1) → S(t2) → ... → S(tn)
```

Nexus studies whether two observations that look similar at the present can contain different information about the future because they arrived there through different trajectories.

## Current experiment

### Experiment 003 — Adversarial Synthetic World

The current software experiment is designed to attack the hypothesis.

It compares:

1. **Ordered world** — temporal order is preserved.
2. **Shuffled-time control** — the same observations are reordered.
3. **Null world** — observations do not arise from a progressing trajectory.

The experiment also introduces noise and missing observations.

A temporal claim becomes interesting only if the apparent advantage depends on temporal structure, weakens when order is destroyed, and does not appear systematically in a world without temporal information.

See [docs/experiment-003.md](docs/experiment-003.md).

## Architecture

```
OBSERVATIONS
     ↓
QUALITY / PROVENANCE
     ↓
CELL SIGNATURES
     ↓
TEMPORAL ORDER
     ↓
TRAJECTORY
     ↓
STATE-CHANGE FEATURES
     ↓
COMPARATIVE INFERENCE
     ↓
UNCERTAINTY
     ↓
HUMAN REVIEW
```

The architecture keeps measurement, representation, inference and interpretation separate.

## Research objects

### Cell Signature

A versioned multimodal representation of one observation.

### Cell State Trajectory

An ordered sequence of signatures belonging to the same research entity.

### Adversarial World

A controlled synthetic environment used to determine whether the temporal hypothesis survives falsification attempts.

## Repository

```
nexus_brain/
├── signature.py       # multimodal observation contract
├── trajectory.py      # transparent trajectory mathematics
├── synthetic.py       # deterministic synthetic world
├── adversarial.py     # temporal, shuffled and null controls
└── safety.py          # conservative research evidence states

experiments/
└── 003_adversarial_world.py

docs/
├── architecture.md
├── scientific-framework.md
├── experiment-003.md
├── research-roadmap.md
├── safety-model.md
└── cell-signature.schema.json

tests/
└── test_core.py
```

## Scientific rules

- No future observation may enter a past prediction.
- Ground truth remains separate from model inputs.
- Snapshot-only baselines remain mandatory.
- Temporal order must be tested explicitly.
- Null worlds must be tested.
- Noise and missingness must be visible.
- Random seeds and versions must be reproducible.
- Negative results are valid outcomes.
- Synthetic results are not biological or clinical evidence.
- No autonomous treatment or medical action is part of this repository.

## What Nexus does not currently claim

The project does not currently claim to diagnose disease, detect cancer, predict individual clinical outcomes, remove abnormal cells, or provide treatment.

Those questions require biological evidence that does not yet exist in this codebase.

## Status

**Research prototype — temporal hypothesis under adversarial testing.**

The immediate objective is not to maximize a benchmark score. It is to determine whether the central hypothesis survives attempts to prove it wrong.

## Long-term direction

Only if the computational hypothesis survives rigorous tests should the project move toward real longitudinal biological datasets, laboratory measurements, microfluidics, or any extracorporeal hardware concept.

The computational hypothesis comes first.
