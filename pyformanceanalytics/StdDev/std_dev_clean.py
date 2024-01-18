"""An enumeration for the std dev clean."""
from enum import Enum


class StdDevClean(Enum):
    NONE = "none"
    BOUDT = "boudt"
    GELTNER = "geltner"
    LOCSCALEROB = "locScaleRob"
