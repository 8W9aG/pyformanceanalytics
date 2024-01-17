"""An enumeration for the VaR methods."""
from enum import Enum


class VaRMethod(Enum):
    MODIFIED = "modified"
    GAUSSIAN = "gaussian"
    HISTORICAL = "historical"
    KERNEL = "kernel"
