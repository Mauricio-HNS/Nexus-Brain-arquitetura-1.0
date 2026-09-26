# Experiment 003 — Adversarial Synthetic World

## Purpose

Experiment 003 is designed to attack the central Nexus hypothesis.

The question is not whether the trajectory heuristic can produce a positive
number. The question is whether any observed advantage depends on genuine
temporal structure rather than extra observations, noise artifacts, or a
construction bias in the synthetic generator.

## Controls

### 1. Ordered world

The observations remain in their original temporal order.

This is the condition in which a temporal signal is allowed to exist.

### 2. Shuffled-time control

The same observations are randomly reordered before the trajectory score is
calculated.

If the trajectory advantage remains essentially unchanged after shuffling,
the result may be caused by having multiple observations rather than by their
temporal order.

### 3. Null world

Observations are generated independently rather than from a progressing latent
trajectory.

A temporal method should not systematically create an advantage in a world
where temporal structure contains no predictive information.

### 4. Noise and missingness

The benchmark introduces observation noise and missing values.

The objective is to measure degradation explicitly rather than silently
discard difficult observations.

## Falsification logic

A stronger result would require all of the following:

- ordered trajectories show reproducible additional information;
- the advantage decreases when temporal order is destroyed;
- the null world does not produce the same advantage;
- performance remains interpretable under noise and missingness;
- results are reproducible across independent seeds.

Failure of any of these conditions is evidence against the current hypothesis or
against the current implementation.

## Important limitation

This experiment is still entirely synthetic. It does not establish that real
cells behave this way, that temporal measurements improve disease detection,
or that any clinical outcome can be predicted.

The purpose is narrower:

> determine whether the proposed computational idea survives adversarial controls
> before investing in biological integration.

## Next step

If Experiment 003 survives its controls, the next milestone should move toward
public longitudinal biological datasets and task definitions with real,
independent ground truth.
