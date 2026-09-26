# Nexus Brain Architecture

## 1. System layers

### Data layer
Receives observations from laboratory instruments, curated datasets, or simulations. Raw observations must retain provenance and acquisition metadata.

### Feature layer
Converts heterogeneous observations into normalized features while preserving the original measurements.

### Signature layer
Builds a versioned `CellSignature` from multimodal features.

### Intelligence layer
Runs modality-specific models and a fusion model. Models must expose confidence/uncertainty and version information.

### Temporal layer
Compares observations over time to detect meaningful changes rather than relying only on a single snapshot.

### Safety layer
Applies conservative rules, detects conflicts, prevents unsupported autonomous actions, and records every decision path.

### Human review layer
Presents evidence, provenance, confidence, and model explanations to qualified researchers/clinicians.

## 2. Decision state machine

```text
INPUT
  |
  v
OBSERVE
  |
  v
FEATURE EXTRACTION
  |
  v
SIGNATURE BUILD
  |
  v
MULTIMODAL FUSION
  |
  +----> insufficient evidence ----> UNKNOWN / OBSERVE
  |
  +----> conflicting evidence ----> REVIEW
  |
  +----> validated research pattern -> FLAG FOR REVIEW
```

The state machine intentionally has no autonomous therapeutic branch.

## 3. Design requirements

- deterministic preprocessing where possible;
- versioned schemas;
- model version tracking;
- dataset provenance;
- reproducible experiments;
- calibration and uncertainty evaluation;
- explicit unknown state;
- audit logs;
- separation between research inference and clinical decision-making.

## 4. Future interfaces

The architecture should expose stable contracts for:

```text
Laboratory Instrument
        |
        v
Observation Adapter
        |
        v
Cell Observation
        |
        v
Cell Signature
        |
        v
Inference Pipeline
```

Future hardware must not require the AI core to know how a particular instrument physically operates.
