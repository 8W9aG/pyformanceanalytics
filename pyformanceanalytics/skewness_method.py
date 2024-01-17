"""An enumeration for the skewness methods."""
from enum import Enum


class SkewnessMethod(Enum):
    MOMENT = "moment"
    FISHER = "fisher"
    SAMPLE = "sample"
