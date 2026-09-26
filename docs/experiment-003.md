# Experiment 003 — Adversarial Synthetic World

## Objective

Try to break the Nexus temporal hypothesis before introducing real biological data.

The experiment asks whether an apparent trajectory advantage is caused by genuine temporal structure or by artifacts of the benchmark.

## Conditions

### Ordered

The synthetic observations remain in their original temporal order.

### Shuffled time

The exact same observations are randomly reordered.

This preserves the observations while destroying their original temporal sequence.

If the advantage remains unchanged, the result may not depend on temporal structure.

### Null world

Observations are generated independently rather than from a progressing latent trajectory.

A temporal method should not systematically gain information from history when the history contains no predictive temporal structure.

## Perturbations

- measurement noise;
- missing values;
- independent random seeds.

## Interpretation

A useful temporal signal should show a measurable difference between ordered and shuffled conditions and should not appear systematically in the null world.

This experiment does not prove biological validity. It only tests whether the computational hypothesis survives controlled adversarial conditions.

## Next experiment

If the controls survive, the next question is stronger:

> Can two entities with similar current snapshots have different futures because their preceding trajectories are different?

That becomes the next falsifiable experiment.
