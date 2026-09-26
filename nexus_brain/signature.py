"""Core domain model for multimodal cellular observations.

This module deliberately contains no clinical interpretation. It provides a
stable research representation that can be consumed by future models.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class CellSignature:
    """Multimodal representation of one research observation."""

    observation_id: str
    morphology: dict[str, Any] = field(default_factory=dict)
    surface_markers: dict[str, Any] = field(default_factory=dict)
    proteomics: dict[str, Any] = field(default_factory=dict)
    transcriptomics: dict[str, Any] = field(default_factory=dict)
    genomics: dict[str, Any] = field(default_factory=dict)
    metabolism: dict[str, Any] = field(default_factory=dict)
    physical_properties: dict[str, Any] = field(default_factory=dict)
    temporal: dict[str, Any] = field(default_factory=dict)
    provenance: dict[str, Any] = field(default_factory=dict)

    def modalities(self) -> dict[str, dict[str, Any]]:
        """Return all modalities using stable API names."""
        return {
            "morphology": self.morphology,
            "surfaceMarkers": self.surface_markers,
            "proteomics": self.proteomics,
            "transcriptomics": self.transcriptomics,
            "genomics": self.genomics,
            "metabolism": self.metabolism,
            "physicalProperties": self.physical_properties,
            "temporal": self.temporal,
        }

    def to_dict(self) -> dict[str, Any]:
        """Serialize the signature for experiments and model pipelines."""
        return {
            "schemaVersion": "1.0",
            "observationId": self.observation_id,
            "modalities": self.modalities(),
            "provenance": self.provenance,
        }
