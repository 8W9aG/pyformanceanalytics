"""An enumeration for the regression fit."""
from enum import Enum


class RegressionFit(Enum):
    LOESS = "loess"
    LINEAR = "linear"
    CONDITIONAL = "conditional"
    QUADRATIC = "quadratic"
