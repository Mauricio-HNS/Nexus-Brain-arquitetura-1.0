# Experiment 002 — Snapshot vs Trajectory

## Purpose

Test whether temporal information produces a measurable computational advantage over a snapshot-only representation in the controlled synthetic world.

## Comparison

- Snapshot baseline: latest available observation only.
- Trajectory baseline: ordered history.

The final observation is held out from both predictors.

## Critical control

Shuffle temporal order. If the advantage remains after shuffling, the experiment may be measuring access to more observations rather than temporal structure.

## Required extensions

- higher noise;
- missing observations;
- missing modalities;
- shorter trajectories;
- distribution shift;
- a null world where time adds no information.

A positive synthetic result is software evidence only, not biological or clinical evidence.
