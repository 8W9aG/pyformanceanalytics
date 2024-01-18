"""An enumeration for the sharpe ratio function."""
from enum import Enum


class SharpeRatioFunction(Enum):
    STD_DEV = "StdDev"
    VAR = "VaR"
    ES = "ES"
