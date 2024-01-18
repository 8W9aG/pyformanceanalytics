"""An enumeration for the rolling regression attribute."""
from enum import Enum


class RollingRegressionAttribute(Enum):
    BETA = "Beta"
    ALPHA = "Alpha"
    RSQUARED = "R-Squared"
