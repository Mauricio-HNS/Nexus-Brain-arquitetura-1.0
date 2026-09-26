# Nexus Brain Safety Model

Nexus is a research system. Its safety model is designed to prevent computational outputs from being mistaken for biological or clinical conclusions.

## Core states

```
UNKNOWN
   ↓
OBSERVE
   ↓
REVIEW
   ↓
FLAG FOR REVIEW
```

These states describe research evidence handling only.

## Rules

- Missing confidence or uncertainty → UNKNOWN.
- Conflicting modalities → REVIEW.
- High uncertainty → OBSERVE.
- Strong research signal with low uncertainty → FLAG FOR REVIEW.
- No state authorizes treatment.

## Provenance requirements

Every inference should retain:

- model version;
- feature/trajectory pipeline version;
- generator or dataset version;
- input quality;
- missing modalities;
- confidence;
- uncertainty;
- timestamp;
- decision state;
- audit identifier.

## Failure philosophy

The system should prefer:

**abstention > unsupported certainty**

A model is allowed to say:

> **I do not have enough evidence.**

That behavior is a feature, not a failure.

## Future translation

Any transition toward medical use would require independent biological validation, safety engineering, regulatory review, and appropriately designed preclinical and clinical studies.
