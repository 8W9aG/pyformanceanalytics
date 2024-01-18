"""An enumeration for the upside risk stat."""
from enum import Enum


class UpsideRiskStat(Enum):
    RISK = "risk"
    VARIANCE = "variance"
    POTENTIAL = "potential"
