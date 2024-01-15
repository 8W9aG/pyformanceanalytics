"""The PerformanceAnalytics average length function."""
import pandas as pd
from rpy2 import robjects

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def average_length(R: pd.DataFrame) -> float:
    """Calculate AverageLength."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return robjects.r("AverageLength").rcall(
            (
                ("R", xts_from_df(R)),
            ),
            lc,
        )[0]
