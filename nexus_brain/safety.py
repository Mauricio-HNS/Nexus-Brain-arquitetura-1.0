"""Research-only safety state machine.

The engine intentionally abstains when evidence is insufficient or conflicting.
It does not authorize treatment or autonomous medical action.
"""

from dataclasses import dataclass
from enum import Enum


class EvidenceState(str, Enum):
    UNKNOWN = "unknown"
    OBSERVE = "observe"
    REVIEW = "review"
    FLAG = "flag_for_review"


@dataclass(frozen=True, slots=True)
class SafetyDecision:
    state: EvidenceState
    reason: str


def evaluate_evidence(
    *,
    confidence: float | None,
    uncertainty: float | None,
    conflicting_modalities: bool = False,
) -> SafetyDecision:
    """Convert research-model evidence into a conservative review state."""
    if confidence is None or uncertainty is None:
        return SafetyDecision(EvidenceState.UNKNOWN, "missing confidence or uncertainty")

    if not 0 <= confidence <= 1 or not 0 <= uncertainty <= 1:
        raise ValueError("confidence and uncertainty must be between 0 and 1")

    if conflicting_modalities:
        return SafetyDecision(EvidenceState.REVIEW, "conflicting modality evidence")

    if uncertainty >= 0.40:
        return SafetyDecision(EvidenceState.OBSERVE, "uncertainty is too high")

    if confidence >= 0.80 and uncertainty < 0.20:
        return SafetyDecision(EvidenceState.FLAG, "strong research signal; human review required")

    return SafetyDecision(EvidenceState.OBSERVE, "insufficient evidence for a research flag")
