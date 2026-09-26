# 🧬 Nexus Brain

### Cell-State Intelligence • Multimodal AI • Longitudinal Biology

> **A research architecture for studying whether the trajectory of a cell contains predictive information that is invisible in an isolated snapshot.**

[![Status](https://img.shields.io/badge/status-research%20prototype-0b7285)](#status)
[![Research](https://img.shields.io/badge/research-cell--state%20trajectory-6d28d9)](#the-core-hypothesis)
[![Python](https://img.shields.io/badge/python-3.12-3776ab)](#technology)
[![Safety](https://img.shields.io/badge/AI-abstention--first-2e7d32)](#safety)

---

## The new direction

**Nexus Brain** is the computational research core of the broader **Nexus Cell** concept.

The project is no longer centered on building another generic multimodal classifier.

Its central hypothesis is:

> **A cell is not only a state. It is a trajectory.**

A snapshot asks:

> **What is this cell?**

Nexus asks:

> **How is this cell changing, and can its multimodal trajectory reveal a meaningful state transition before the final state becomes obvious?**

That is the scientific question we intend to test.

**This repository is research software. It is not a medical device, diagnostic system, or validated treatment.**

---

## 🔬 The core hypothesis

A conventional pipeline often looks like:

```
OBSERVATION → CLASSIFICATION
```

Nexus investigates:

```
OBSERVATION T0
      ↓
OBSERVATION T1
      ↓
OBSERVATION T2
      ↓
OBSERVATION T3
      ↓
CELL TRAJECTORY
      ↓
STATE TRANSITION SIGNAL
```

The important object is therefore not only the **Cell Signature**, but the **Cell State Trajectory**:

```
Cell Signature
      +
time
      +
change
      +
multimodal evidence
      ↓
CELL STATE TRAJECTORY
```

The first scientific milestone is not to claim that Nexus can detect disease.

It is to determine whether this representation contains information that isolated snapshots do not.

---

## 🧠 Architecture

```
                         NEXUS BRAIN
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
          CELL SIGNATURE            TEMPORAL ENGINE
                 │                         │
                 └────────────┬────────────┘
                              ▼
                    TRAJECTORY BUILDER
                              │
                              ▼
                    STATE TRANSITION MAP
                              │
                  ┌───────────┴───────────┐
                  ▼                       ▼
             STABLE STATE          TRANSITION SIGNAL
                                          │
                              ┌───────────┴───────────┐
                              ▼                       ▼
                         UNCERTAINTY              BASELINES
                              │                       │
                              └───────────┬───────────┘
                                          ▼
                                    SAFETY ENGINE
                                          │
                                          ▼
                                   HUMAN REVIEW
```

The architecture deliberately separates:

**measurement → representation → trajectory → inference → validation**

No component is allowed to silently turn a research signal into a clinical conclusion.

---

## 🧬 Cell Signature

The Cell Signature remains the multimodal representation of an observation:

```
CellSignature
│
├── morphology
├── surface markers
├── proteomics
├── transcriptomics
├── genomics
├── metabolism
├── physical properties
├── temporal context
└── provenance / uncertainty
```

But Nexus adds another layer:

```
SIGNATURE T0 ──┐
SIGNATURE T1 ──┤
SIGNATURE T2 ──┼──→ TRAJECTORY
SIGNATURE T3 ──┤
SIGNATURE T4 ──┘
```

---

## 🔭 The research question

> **Can multimodal temporal representations detect a controlled cellular state transition earlier or more reliably than isolated observations?**

This is falsifiable.

A meaningful result would require the trajectory model to outperform appropriate snapshot baselines under controlled experiments, while preserving calibration and abstention behavior.

A negative result is also scientifically useful: it would tell us that the proposed representation does not provide the expected additional information under the tested conditions.

---

## 🧪 Experiment 001 — Cell State Trajectory

The first experiment is deliberately small.

We create synthetic cells with known hidden states and generate a sequence of observations.

```
T0 → T1 → T2 → T3 → T4
│                   │
│                   └── hidden future state
│
└── observations available to the model
```

The model must not see the future label.

We compare:

1. **Snapshot baseline** — uses only the current observation.
2. **Trajectory baseline** — uses the history of observations.
3. **Missing-data conditions**.
4. **Noise conditions**.
5. **Distribution-shift conditions**.

The experiment asks whether temporal information actually adds measurable signal.

---

## 🧱 Research layers

### Layer 1 — Measurement representation

Convert heterogeneous observations into reproducible signatures.

### Layer 2 — State representation

Represent the current cellular state without assuming a clinical label.

### Layer 3 — Trajectory representation

Measure how the state changes over time.

### Layer 4 — Transition detection

Identify statistically meaningful changes in the trajectory.

### Layer 5 — Validation

Test against controlled ground truth and independent datasets.

Only after these layers produce reproducible evidence should biological or hardware integration become a serious engineering target.

---

## 🛡️ Safety principles

Nexus is **abstention-first**.

- Unknown is not abnormal.
- Abnormal is not automatically malignant.
- A model score is not biological truth.
- A trajectory signal is not a diagnosis.
- Conflicting evidence lowers confidence.
- Missing data must remain visible.
- Every inference retains provenance and version information.
- No autonomous therapeutic action exists in the architecture.
- Synthetic experiments are software validation, not clinical evidence.

---

## 🧱 Repository structure

```
Nexus-Brain-arquitetura-1.0/
│
├── nexus-brain/
│   ├── signature.py
│   ├── fusion.py
│   ├── trajectory.py
│   ├── synthetic.py
│   └── safety.py
│
├── experiments/
│   └── 001_cell_state_trajectory.py
│
├── tests/
│   └── test_core.py
│
├── docs/
│   ├── README.md
│   ├── architecture.md
│   ├── scientific-framework.md
│   ├── experimental-protocol.md
│   ├── research-roadmap.md
│   ├── safety-model.md
│   └── cell-signature.schema.json
│
└── .github/workflows/
    └── quality.yml
```

---

## ⚙️ Technology

The scientific core is intentionally lightweight at this stage.

| Layer | Direction |
|---|---|
| Research core | Python |
| Future ML | PyTorch |
| Experiment APIs | FastAPI |
| Production services | C# / .NET |
| Data | PostgreSQL |
| Streaming | Kafka-compatible architecture |
| Research UI | React |
| Infrastructure | Docker |
| Reproducibility | versioned code, seeds, datasets and artifacts |

Dependencies should be introduced only when they provide measurable scientific value.

---

## 📚 Scientific standard

Nexus follows:

**Measurement → Feature → Signature → Trajectory → Inference → Validation → Biological interpretation**

The project explicitly rejects the idea that:

- a polished demo is proof;
- synthetic accuracy is clinical evidence;
- correlation automatically means causation;
- model confidence equals biological certainty.

The goal is to build experiments that can prove the idea wrong.

---

## 🚧 Status

**Research architecture — trajectory-first redesign**

Current milestone:

> **Experiment 001: Cell State Trajectory**

The immediate objective is to establish whether temporal multimodal information adds measurable predictive value over a snapshot-only baseline.

---

## 🌐 Long-term Nexus Cell vision

If the computational hypothesis survives rigorous testing, the architecture could eventually become the intelligence layer behind validated biological measurement systems.

Only then would it make sense to investigate laboratory instrumentation, microfluidics, or extracorporeal platforms.

The machine is not the starting point.

**The scientific brain is.**

---

## License

License and contribution policy will be defined as the research architecture matures.
