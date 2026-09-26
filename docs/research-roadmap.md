# Research Roadmap

## Stage 1 — Adversarial synthetic validation

Current stage.

Establish whether temporal information survives shuffled-time and null-world controls.

## Stage 2 — Same snapshot, different trajectory

Construct controlled cases where the current state is intentionally similar while preceding trajectories differ.

Test whether trajectory history contains information that a snapshot cannot recover.

## Stage 3 — Multimodal dynamics

Introduce modalities with different noise, missingness and correlation structures.

Test whether temporal information remains useful when individual modalities become unreliable.

## Stage 4 — Real longitudinal datasets

Move to authorized public datasets with real repeated biological measurements and independent ground truth.

Requirements include documented provenance, licensing, subject-level separation where applicable, and strict leakage controls.

## Stage 5 — Independent biological validation

Test across datasets, instruments, acquisition protocols and laboratories.

## Stage 6 — Physical-system research

Only after computational and biological evidence supports the approach should the project investigate instrumentation, microfluidics or extracorporeal systems.

## Kill criteria

Stop or redesign the approach if:

1. temporal history adds no reproducible information;
2. apparent gains survive time destruction;
3. the null world produces comparable gains;
4. results depend on leakage;
5. results fail under realistic noise;
6. independent reproduction fails.

The project earns continuation through evidence.
