# Nexus Brain — Experiment 001

## Cell State Trajectory

### Objective

Test whether a sequence of multimodal observations can predict a controlled future state more effectively than the current observation alone.

### Core comparison

**Baseline A — Snapshot**

Uses only the current observation.

**Baseline B — Trajectory**

Uses the ordered history of observations.

The experiment is intentionally simple enough that the result can be inspected and reproduced.

## Synthetic world

Each research entity receives a latent state that evolves over time.

The simulator produces observable modality values from that latent state while adding controlled noise.

The future state is hidden from the predictor.

### Example

```
latent state
   ↓
T0 observation
   ↓
T1 observation
   ↓
T2 observation
   ↓
T3 observation
   ↓
future state
```

The predictor receives T0...T3 and must infer the future state without seeing it.

## Experimental conditions

1. clean observations;
2. measurement noise;
3. missing modalities;
4. short trajectories;
5. distribution shift;
6. independent random seeds.

## Primary metrics

- accuracy;
- balanced accuracy where class imbalance exists;
- precision;
- recall;
- F1;
- calibration;
- abstention rate.

## Scientific controls

The benchmark must report:

- snapshot-only baseline;
- trajectory baseline;
- generator version;
- random seed;
- sample count;
- noise level;
- missingness configuration;
- model configuration.

## Leakage controls

The following are prohibited:

- using future observations;
- using future labels as features;
- calculating normalization parameters from evaluation data;
- tuning on the evaluation set.

## Interpretation

A trajectory advantage is interesting only if it is:

1. reproducible;
2. larger than expected noise;
3. maintained across independent seeds;
4. robust to missing/noisy observations;
5. present without future-information leakage.

No synthetic result is evidence of clinical effectiveness.

## Reproducibility record

```
experiment_id
code_version
generator_version
random_seed
sample_count
noise_level
missingness
model_version
metrics
artifacts
```
