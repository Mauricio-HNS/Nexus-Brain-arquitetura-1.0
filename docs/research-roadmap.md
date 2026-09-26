# Nexus Brain Research Roadmap

## Milestone 001 — Cell State Trajectory

**Objective:** establish whether temporal information adds measurable predictive value over a snapshot-only representation.

Deliverables:

- deterministic synthetic generator;
- trajectory representation;
- snapshot baseline;
- trajectory baseline;
- reproducible benchmark;
- explicit future-label isolation;
- noise and missing-data tests.

## Milestone 002 — Controlled multimodal dynamics

Introduce multiple synthetic modalities with different signal quality and correlation structures.

Questions:

- Which modalities contribute independent information?
- How does the system behave when one modality becomes unreliable?
- Does temporal fusion remain useful when measurements are noisy?

## Milestone 003 — Public research datasets

Move from synthetic observations to authorized/public datasets.

Requirements:

- documented provenance;
- licensing review;
- patient-level split where applicable;
- no leakage across train/validation/test;
- explicit dataset versioning.

## Milestone 004 — Longitudinal validation

Test whether trajectory representations generalize across:

- individuals;
- instruments;
- acquisition protocols;
- laboratories;
- biological populations.

## Milestone 005 — Laboratory integration

Connect validated observation adapters to real measurements.

The computational hypothesis must survive independent biological measurements before any hardware concept is considered.

## Milestone 006 — Nexus Cell systems research

Only after computational and laboratory evidence supports the approach should research address:

- high-throughput cell handling;
- microfluidics;
- extracorporeal circulation;
- real-time analysis;
- selective intervention concepts.

No stage in this roadmap constitutes clinical validation.

---

## Kill criteria

Nexus should be stopped or substantially redesigned if:

1. trajectory information consistently adds no useful signal;
2. apparent gains depend on leakage;
3. gains disappear under realistic noise;
4. results cannot be independently reproduced;
5. the approach does not generalize beyond the synthetic generator.

This is deliberate. The project is designed to earn its continuation through evidence.
