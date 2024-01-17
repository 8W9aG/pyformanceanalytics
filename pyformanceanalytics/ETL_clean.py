"""An enumeration for the ETL cleans."""
from enum import Enum


class ETLCLean(Enum):
    NONE = "none"
    BOUDT = "boudt"
    GELTNER = "geltner"
    LOC_SCALE_ROB = "locScaleRob"
