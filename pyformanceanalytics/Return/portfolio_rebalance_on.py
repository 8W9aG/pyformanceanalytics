"""An enumeration for the portfolio rebalance on method."""
from enum import Enum


class PortfolioRebalanceOn(Enum):
    YEARS = "years"
    QUARTERS = "quarters"
    MONTHS = "months"
    WEEKS = "weeks"
    DAYS = "days"
