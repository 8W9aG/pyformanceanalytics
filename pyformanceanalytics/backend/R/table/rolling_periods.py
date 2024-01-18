"""The PerformanceAnalytics table.RollingPeriods function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def RollingPeriods(
    R: pd.DataFrame,
    periods: (list[int] | None) = None,
    funcs_names: (list[str] | None) = None,
    digits: int = 4,
) -> pd.DataFrame:
    """Calculate table.RollingPeriods."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if periods is None:
        periods = [12, 36, 60]
    if funcs_names is None:
        funcs_names = ["Correlation", "Beta"]
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("table.RollingPeriods").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("periods", ro.vectors.IntVector(periods)),
                    ("funcs.names", ro.vectors.StrVector(funcs_names)),
                    ("digits", digits),
                ),
                lc,
            ),
            lc,
        )
