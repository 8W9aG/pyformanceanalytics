"""An enumeration for the upside potential ratio method."""
from enum import Enum


class UpsidePotentialRatioMethod(Enum):
    SUBSET = "subset"
    FULL = "full"
