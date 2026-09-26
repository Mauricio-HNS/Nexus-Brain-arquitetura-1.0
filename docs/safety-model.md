# Nexus Brain Safety Model

Nexus Brain is designed as a research system with explicit uncertainty and abstention.

## Core rules

```text
No evidence          -> UNKNOWN
Weak evidence        -> OBSERVE
Conflicting evidence -> REVIEW
Strong research signal -> FLAG FOR REVIEW
```

A model output must never be interpreted as a medical diagnosis solely because a classifier assigns a high score.

## Required metadata

Every inference should retain:

- model version;
- feature pipeline version;
- dataset/provenance;
- confidence and uncertainty;
- timestamp;
- input quality indicators;
- decision state;
- audit identifier.

## Failure philosophy

The system should prefer **abstention over unsupported certainty**. Missing or contradictory measurements should reduce confidence rather than trigger escalation.

## Future clinical translation

Any transition from research software to medical use would require independent biological validation, safety engineering, regulatory review, and appropriately designed preclinical and clinical studies.
