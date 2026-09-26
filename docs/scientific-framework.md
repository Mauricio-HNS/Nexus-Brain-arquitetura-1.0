# Scientific Framework

## Central hypothesis

Given a sequence of multimodal observations

```
X0, X1, X2, ..., Xt
```

the temporal trajectory may contain predictive information about a controlled future state that is unavailable from Xt alone.

This is a hypothesis, not an established result.

## Null hypothesis

Temporal history provides no additional predictive information beyond the current snapshot under the tested data-generating process.

## Required evidence

A credible computational result requires:

- snapshot comparison;
- trajectory comparison;
- independent seeds;
- temporal-order controls;
- null-world controls;
- noise and missingness analysis;
- distribution-shift evaluation;
- calibration;
- complete provenance;
- independent reproduction.

## Falsification

The hypothesis should be rejected or redesigned if:

- trajectory information adds no reproducible signal;
- gains survive equally after temporal order is destroyed;
- the null world produces the same apparent advantage;
- gains depend on leakage;
- results collapse under realistic perturbations;
- results cannot be reproduced.

## Scientific boundary

The current repository contains synthetic computational research only. It does not establish biological validity, clinical utility or therapeutic effectiveness.
