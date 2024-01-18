"""An enumeration for the histogram methods."""
from enum import Enum


class HistogramMethods(Enum):
    NONE = "none"
    ADD_DENSITY = "add.density"
    ADD_NORMAL = "add.normal"
    ADD_CENTERED = "add.centered"
    ADD_CAUCHY = "add.cauchy"
    ADD_SST = "add.sst"
    ADD_RUG = "add.rug"
    ADD_RISK = "add.risk"
    ADD_QQPLOT = "add.qqplot"
