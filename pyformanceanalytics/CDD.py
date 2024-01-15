"""The PerformanceAnalytics CDD function."""
import pandas as pd
from rpy2 import robjects

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def CDD(R: pd.DataFrame, geometric: bool = True, invert: bool = True, p: float = 0.95) -> float:
    """Calculate CDD."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return robjects.r("CDD").rcall(
            (
                ("R", xts_from_df(R)),
                ("geometric", geometric),
                ("invert", invert),
                ("p", p),
            ),
            lc,
        )[0]
