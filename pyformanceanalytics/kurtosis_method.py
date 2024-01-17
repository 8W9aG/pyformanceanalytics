"""An enumeration for the skewness methods."""
from enum import Enum


class KurtosisMethod(Enum):
    EXCESS = "excess"
    MOMENT = "moment"
    FISHER = "fisher"
    SAMPLE = "sample"
    SAMPLE_EXCESS = "sample_excess"
