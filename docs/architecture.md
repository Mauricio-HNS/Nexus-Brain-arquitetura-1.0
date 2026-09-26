# Nexus Brain Architecture

## 1. Architectural thesis

Nexus is built around a distinction:

> **A cellular state is an observation. A cellular trajectory is a sequence of observations.**

The architecture therefore treats time as a first-class dimension rather than an optional metadata field.

## 2. System layers

### Layer A — Observation

Raw or curated measurements enter the system through an observation adapter.

```
instrument / dataset / simulator
            ↓
       observation
```

### Layer B — Cell Signature

Each observation is converted into a versioned multimodal representation.

```
morphology
surface markers
proteomics
transcriptomics
genomics
metabolism
physical properties
temporal context
        ↓
CellSignature
```

### Layer C — Trajectory

Multiple signatures belonging to the same tracked research entity are ordered in time.

```
S0 → S1 → S2 → S3 → S4
```

The trajectory engine calculates change rather than only absolute state.

### Layer D — State Transition

The system searches for meaningful changes in the representation:

```
stable → stable → changing → changing → new state
```

A transition signal is a research output, not a diagnosis.

### Layer E — Baselines

Every new approach must be compared with simpler alternatives:

- current snapshot only;
- individual modality;
- pairwise fusion;
- trajectory representation.

The trajectory hypothesis is only interesting if the additional complexity produces measurable information.

### Layer F — Safety

Uncertainty, missing modalities, conflicting measurements, provenance and model versions remain attached to every inference.

### Layer G — Human review

Researchers receive evidence and trajectory context rather than a black-box conclusion.

## 3. Decision flow

```
OBSERVATION
    ↓
QUALITY CONTROL
    ↓
CELL SIGNATURE
    ↓
TEMPORAL ORDERING
    ↓
TRAJECTORY
    ↓
STATE-CHANGE ANALYSIS
    │
    ├── insufficient evidence → UNKNOWN
    ├── unstable/conflicting → REVIEW
    └── reproducible research signal → FLAG FOR REVIEW
```

## 4. Scientific invariants

1. Future observations cannot leak into past prediction.
2. Ground-truth labels must remain separate from model inputs.
3. Snapshot baselines must be reported.
4. Random seeds must be recorded.
5. Missing data must be represented explicitly.
6. Distribution shift must be tested.
7. Model confidence must be calibrated.
8. Every result must be reproducible from versioned inputs.

## 5. Future interfaces

```
Laboratory Instrument
        ↓
Observation Adapter
        ↓
Cell Observation
        ↓
Cell Signature
        ↓
Trajectory Engine
        ↓
Research Inference
        ↓
Human Review
```

Hardware remains outside the computational core until the research evidence justifies integration.
