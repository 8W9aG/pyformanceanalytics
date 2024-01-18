"""An enumeration for the boxplot sort by."""
from enum import Enum


class BoxplotSortBy(Enum):
    MEAN = "mean"
    MEDIAN = "median"
    VARIANCE = "variance"
