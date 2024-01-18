"""An enumeration for the downside deviation method."""
from enum import Enum


class DownsideDeviationMethod(Enum):
    FULL = "full"
    SUBSET = "subset"
