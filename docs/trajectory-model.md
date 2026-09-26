# Cell State Trajectory Model

## Purpose

The trajectory model is the central new abstraction in Nexus Brain.

A **Cell Signature** describes an observation.

A **Cell State Trajectory** describes how a sequence of observations changes over time.

## Representation

```
S(t0) → S(t1) → S(t2) → ... → S(tn)
```

Each state can contain multiple modalities.

The trajectory engine can derive simple research features such as:

- displacement;
- rate of change;
- acceleration/change of rate;
- modality-specific change;
- missingness over time;
- confidence evolution.

## Important distinction

The trajectory is not assumed to represent disease progression.

It represents **observed change**.

Biological interpretation must be established independently.

## Future research

Potential future models include:

- temporal transformers;
- state-space models;
- neural ODE approaches;
- hidden-state models;
- graph-based cell trajectories.

Those should only be introduced when transparent baselines have been exhausted or shown insufficient.

## Scientific requirement

Any advanced model must beat or meaningfully complement a transparent baseline under controlled evaluation.

Complexity is not a scientific contribution by itself.
