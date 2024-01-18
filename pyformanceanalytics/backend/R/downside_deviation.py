"""The PerformanceAnalytics DownsideDeviation function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def DownsideDeviation(
    R: pd.DataFrame,
    MAR: float = 0.0,
    method: (str | None) = None,
    potential: bool = False,
) -> pd.DataFrame | float:
    """Calculate DownsideDeviation."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = "full"
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("DownsideDeviation").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("MAR", MAR),
                    ("method", method),
                    ("potential", potential),
                ),
                lc,
            ),
            lc,
        )
