"""An enumeration for the VaR portfolio methods."""
from enum import Enum


class VaRPortfolioMethod(Enum):
    SINGLE = "single"
    COMPONENT = "component"
    MARGINAL = "marginal"
