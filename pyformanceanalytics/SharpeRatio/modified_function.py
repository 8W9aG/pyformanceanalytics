"""An enumeration for the sharpe ratio function."""
from enum import Enum


class ModifiedFunction(Enum):
    STD_DEV = "StdDev"
    VAR = "VaR"
    ES = "ES"
