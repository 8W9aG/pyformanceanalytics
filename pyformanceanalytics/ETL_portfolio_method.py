"""An enumeration for the ETL portfolio methods."""
from enum import Enum


class ETLPortfolioMethod(Enum):
    SINGLE = "single"
    COMPONENT = "component"
