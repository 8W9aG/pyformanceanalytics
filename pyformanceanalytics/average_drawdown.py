"""The PerformanceAnalytics average drawdown function."""
import pandas as pd
from rpy2 import robjects

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def average_drawdown(R: pd.DataFrame) -> float:
    """Calculate AverageDrawdown."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return robjects.r("AverageDrawdown").rcall(
            (
                ("R", xts_from_df(R)),
            ),
            lc,
        )[0]
