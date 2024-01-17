"""An enumeration for the calculate method."""
from enum import Enum


class CalculateMethod(Enum):
    DISCRETE = "discrete"
    LOG = "log"
    DIFFERENCE = "difference"
