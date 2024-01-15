"""The PerformanceAnalytics MM function."""
import pandas as pd
from rpy2 import robjects

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def mm(R: pd.DataFrame, unbiased: bool = True, as_mat: bool = True) -> float:
    """Calculate MM."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return robjects.r("M3.MM").rcall(
            (
                ("R", xts_from_df(R)),
                ("unbiased", unbiased),
                ("as.mat", as_mat),
            ),
            lc,
        )[0]
