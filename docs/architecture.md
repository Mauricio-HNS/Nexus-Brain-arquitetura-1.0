# Nexus Brain Architecture

## Principle

Nexus treats time as a first-class scientific variable.

```
observation
   ↓
Cell Signature
   ↓
ordered history
   ↓
Cell State Trajectory
   ↓
state-change features
   ↓
research inference
```

## Layers

### 1. Observation

Measurements enter through datasets, simulators or future instrument adapters.

### 2. Cell Signature

Each observation is represented with multimodal fields and provenance.

### 3. Temporal ordering

Observations belonging to the same research entity are ordered using explicit time indices.

### 4. Trajectory

The system represents displacement and rates of change between observations.

### 5. Comparative inference

Trajectory-based representations are compared with simpler snapshot representations.

### 6. Uncertainty

Missing, conflicting or insufficient evidence remains visible.

### 7. Human review

Research signals are presented for investigation. No autonomous medical action exists.

## Scientific invariants

1. No future information leakage.
2. Ground truth is never a feature.
3. Snapshot baselines are mandatory.
4. Time shuffling is a required control.
5. Null worlds are required.
6. Missingness is explicit.
7. Seeds and versions are recorded.
8. Results must be reproducible.
