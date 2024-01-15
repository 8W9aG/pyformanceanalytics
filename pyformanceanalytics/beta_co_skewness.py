"""The PerformanceAnalytics beta co skewness function."""
import pandas as pd
from rpy2 import robjects

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def beta_co_skewness(Ra: pd.DataFrame, Rb: pd.DataFrame) -> float:
    """Calculate BetaCoSkewness."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return robjects.r("BetaCoSkewness").rcall(
            (
                ("Ra", xts_from_df(Ra)),
                ("Rb", xts_from_df(Rb)),
            ),
            lc,
        )[0]
