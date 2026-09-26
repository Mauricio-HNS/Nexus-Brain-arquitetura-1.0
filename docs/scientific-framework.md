# Nexus Scientific Framework

## Central question

> **Can the temporal trajectory of a multimodal cellular representation provide predictive information about a future cellular state that is not available from an isolated snapshot?**

This is the central Nexus hypothesis.

## Why this question matters

Many biological measurements are snapshots. A snapshot can describe what was observed at a particular moment.

Nexus asks whether the **direction and rate of change** across repeated observations carry additional information.

Conceptually:

```
SNAPSHOT
What is observed now?

TRAJECTORY
How is the observed state changing?
```

The second question is not automatically more informative. That is exactly what the experiment must establish.

## Falsifiable hypothesis

Given a sequence:

```
X0, X1, X2, ..., Xt
```

where each X is a multimodal Cell Signature, a trajectory representation may predict a controlled future state better than a model receiving only Xt.

The hypothesis is supported only if the difference survives appropriate baselines, repeated seeds, noise tests and distribution-shift evaluation.

## Null hypothesis

Temporal history provides no additional predictive information beyond the current snapshot under the tested data-generating process.

The project must actively attempt to reproduce this null.

## Evidence hierarchy

```
RAW MEASUREMENT
      ↓
QUALITY CONTROL
      ↓
FEATURE
      ↓
CELL SIGNATURE
      ↓
TRAJECTORY
      ↓
MODEL INFERENCE
      ↓
VALIDATION
      ↓
BIOLOGICAL INTERPRETATION
```

## Minimum evidence standard

A convincing computational result should include:

- independent random seeds;
- explicit train/evaluation separation;
- no future-label leakage;
- snapshot baseline;
- trajectory baseline;
- missing-data tests;
- noise robustness;
- distribution-shift tests;
- calibration;
- false-positive and false-negative analysis;
- complete experiment provenance.

## What would invalidate the hypothesis?

Examples include:

- trajectory models provide no reproducible improvement over snapshot baselines;
- improvement disappears under small distribution changes;
- the result depends on future information leaking into the input;
- calibration deteriorates substantially;
- synthetic patterns do not survive independent datasets.

A negative result is a valid scientific outcome.

## What the project does not claim

Nexus does not currently claim to:

- diagnose cancer;
- detect every disease;
- identify malignant cells in real time;
- predict an individual's clinical outcome;
- remove abnormal cells from blood;
- provide medical treatment.

Those are future questions that would require substantially different evidence.

## Long-term objective

Build a computational framework whose assumptions, experiments and failures are visible enough that independent researchers can reproduce and challenge them.
