"""An enumeration for the VaR cleans."""
from enum import Enum


class VaRClean(Enum):
    NONE = "none"
    BOUDT = "boudt"
    GELTNER = "geltner"
    LOC_SCALE_ROB = "locScaleRob"
