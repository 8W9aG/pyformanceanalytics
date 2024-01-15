"""The PerformanceAnalytics sterling ratio function."""
import pandas as pd
from rpy2 import robjects

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def sterling_ratio(R: pd.DataFrame, excess: float = 0.1) -> float:
    """Calculate SterlingRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return robjects.r("SterlingRatio").rcall(
            (
                ("R", xts_from_df(R)),
                ("excess", excess),
            ),
            lc,
        )[0]
