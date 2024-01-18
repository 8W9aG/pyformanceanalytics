"""An enumeration for the bar va r method."""
from enum import Enum


class BarVaRMethod(Enum):
    NONE = "none"
    MODIFIEDVAR = "ModifiedVaR"
    GAUSSIANVAR = "GaussianVaR"
    HISTORICALVAR = "HistoricalVaR"
    STDDEV = "StdDev"
    MODIFIEDES = "ModifiedES"
    GAUSSIANES = "GaussianES"
    HISTORICALES = "HistoricalES"
