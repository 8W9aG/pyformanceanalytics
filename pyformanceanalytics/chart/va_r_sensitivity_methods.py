"""An enumeration for the VaRSensitivity Methods."""
from enum import Enum


class VaRSensitivityMethods(Enum):
    GAUSSIANVAR = "GaussianVaR"
    MODIFIEDVAR = "ModifiedVaR"
    HISTORICALVAR = "HistoricalVaR"
    GAUSSIANES = "GaussianES"
    MODIFIEDES = "ModifiedES"
    HISTORICALES = "HistoricalES"
