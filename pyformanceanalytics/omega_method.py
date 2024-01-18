"""An enumeration for the Omega methods."""
from enum import Enum


class OmegaMethod(Enum):
    SIMPLE = "simple"
    INTERP = "interp"
    BINOMIAL = "binomial"
    BLACKSCHOLES = "blackscholes"
