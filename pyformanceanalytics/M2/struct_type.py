"""An enumeration for the struct type."""
from enum import Enum


class StructType(Enum):
    INDEP = "Indep"
    INDEPID = "IndepId"
    OBSERVEDFACTOR = "observedfactor"
    CC = "CC"
