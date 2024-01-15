"""The PerformanceAnalytics MM function."""
import pandas as pd
from rpy2 import robjects

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def mm(R: pd.DataFrame, as_mat: bool = True) -> float:
    """Calculate MM."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return robjects.r("M4.MM").rcall(
            (
                ("R", xts_from_df(R)),
                ("as.mat", as_mat),
            ),
            lc,
        )[0]
