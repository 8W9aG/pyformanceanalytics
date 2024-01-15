"""The PerformanceAnalytics bernardo ledoit ratio function."""
import pandas as pd
from rpy2 import robjects

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def bernardo_ledoit_ratio(R: pd.DataFrame) -> float:
    """Calculate BernardoLedoitRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return robjects.r("BernardoLedoitRatio").rcall(
            (
                ("R", xts_from_df(R)),
            ),
            lc,
        )[0]
