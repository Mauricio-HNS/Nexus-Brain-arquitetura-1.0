# Cell State Trajectory

## Definition

A Cell Signature represents one observation.

A Cell State Trajectory represents ordered observations from the same research entity:

```
S(t0) → S(t1) → S(t2) → ... → S(tn)
```

## Current features

The transparent baseline calculates:

- displacement;
- mean velocity;
- change in velocity.

These are mathematical descriptors of observed change. They are not disease markers.

## Future models

Potential research models include state-space models, temporal transformers, neural differential-equation approaches and graph-based trajectory methods.

They should be introduced only when a transparent baseline is insufficient and the added complexity can be justified experimentally.
