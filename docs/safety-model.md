# Research Safety Model

Nexus Brain is research software.

## Evidence states

```
UNKNOWN → OBSERVE → REVIEW
                    ↓
              FLAG FOR REVIEW
```

These states describe research evidence handling only.

## Rules

- Missing confidence or uncertainty produces UNKNOWN.
- Conflicting evidence produces REVIEW.
- High uncertainty produces OBSERVE.
- A strong research signal remains a human-review state.
- No state authorizes treatment or autonomous intervention.

## Provenance

Future inference records should retain model version, data version, pipeline version, input quality, missingness, uncertainty and experiment identifier.

## Boundary

A computational signal is not a diagnosis.

Any future medical translation would require independent biological validation, safety engineering and the appropriate regulatory and clinical evidence.
