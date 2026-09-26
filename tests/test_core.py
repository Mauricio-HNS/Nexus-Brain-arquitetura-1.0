from nexus_brain.fusion import fuse_modalities
from nexus_brain.safety import EvidenceState, evaluate_evidence
from nexus_brain.signature import CellSignature
from nexus_brain.synthetic import generate_trajectory
from nexus_brain.trajectory import TrajectoryPoint, summarize_trajectory


def test_signature_serialization():
    signature = CellSignature(
        observation_id="synthetic-001",
        morphology={"size": 1.0},
        provenance={"sourceType": "synthetic"},
    )
    data = signature.to_dict()
    assert data["schemaVersion"] == "1.0"
    assert data["observationId"] == "synthetic-001"
    assert data["provenance"]["sourceType"] == "synthetic"


def test_fusion_is_transparent():
    result = fuse_modalities({"morphology": 0.8, "proteomics": 0.6})
    assert result["aggregate"] == 0.7
    assert result["coverage"] == 0.25


def test_missing_evidence_abstains():
    decision = evaluate_evidence(confidence=None, uncertainty=None)
    assert decision.state is EvidenceState.UNKNOWN


def test_conflicting_evidence_requires_review():
    decision = evaluate_evidence(
        confidence=0.99,
        uncertainty=0.01,
        conflicting_modalities=True,
    )
    assert decision.state is EvidenceState.REVIEW


def test_strong_research_signal_requires_review():
    decision = evaluate_evidence(confidence=0.90, uncertainty=0.10)
    assert decision.state is EvidenceState.FLAG


def test_trajectory_is_deterministic():
    first = generate_trajectory(entity_id="cell-a", seed=123)
    second = generate_trajectory(entity_id="cell-a", seed=123)
    assert first == second


def test_trajectory_changes_when_seed_changes():
    first = generate_trajectory(entity_id="cell-a", seed=123)
    second = generate_trajectory(entity_id="cell-a", seed=124)
    assert first != second


def test_trajectory_summary():
    points = [
        TrajectoryPoint(time_index=0, values=(0.0, 0.0)),
        TrajectoryPoint(time_index=1, values=(1.0, 0.0)),
        TrajectoryPoint(time_index=2, values=(3.0, 0.0)),
    ]
    summary = summarize_trajectory(points)
    assert round(summary.displacement, 6) == 3.0
    assert round(summary.velocity, 6) == 1.5
    assert round(summary.acceleration, 6) == 1.0
