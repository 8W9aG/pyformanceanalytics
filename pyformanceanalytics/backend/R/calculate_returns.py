"""The PerformanceAnalytics CalculateReturns function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def CalculateReturns(prices: pd.DataFrame, method: str) -> pd.DataFrame | float:
    """Calculate CalculateReturns."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("CalculateReturns").rcall(  # type: ignore
                (
                    ("prices", xts_from_df(prices)),
                    ("method", method),
                ),
                lc,
            ),
            lc,
        )
