"""An enumeration for the correlation method."""
from enum import Enum


class CorrelationMethod(Enum):
    PEARSON = "pearson"
    KENDALL = "kendall"
    SPEARMAN = "spearman"
