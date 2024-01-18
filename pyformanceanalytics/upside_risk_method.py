"""An enumeration for the upside risk method."""
from enum import Enum


class UpsideRiskMethod(Enum):
    FULL = "full"
    SUBSET = "subset"
