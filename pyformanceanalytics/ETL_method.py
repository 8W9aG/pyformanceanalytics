"""An enumeration for the ETL methods."""
from enum import Enum


class ETLMethod(Enum):
    MODIFIED = "modified"
    GAUSSIAN = "gaussian"
    HISTORICAL = "historical"
