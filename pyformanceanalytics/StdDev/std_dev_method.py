"""An enumeration for the std dev method."""
from enum import Enum


class StdDevMethod(Enum):
    PEARSON = "pearson"
    KENDALL = "kendall"
    SPEARMAN = "spearman"
