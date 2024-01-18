"""An enumeration for the qq plot lines."""
from enum import Enum


class QQPlotLine(Enum):
    QUARTILES = "quartiles"
    ROBUST = "robust"
    NONE = "none"
