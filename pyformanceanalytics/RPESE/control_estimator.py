"""An enumeration for the control estimator."""
from enum import Enum


class ControlEstimator(Enum):
    MEAN = "Mean"
    SD = "SD"
    VaR = "VaR"
    ES = "ES"
    SR = "SR"
    SoR = "SoR"
    ESratio = "ESratio"
    VaRratio = "VaRratio"
    LPM = "LPM"
    OmegaRatio = "OmegaRatio"
    SemiSD = "SemiSD"
    RachevRatio = "RachevRatio"
