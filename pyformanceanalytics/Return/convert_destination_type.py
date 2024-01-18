"""An enumeration for the convert destination type."""
from enum import Enum


class ConvertDestinationType(Enum):
    DISCRETE = "discrete"
    LOG = "log"
    DIFFERENCE = "difference"
    LEVEL = "level"
