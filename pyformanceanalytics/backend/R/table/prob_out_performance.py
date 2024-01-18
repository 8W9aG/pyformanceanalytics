"""The PerformanceAnalytics table.ProbOutPerformance function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def ProbOutPerformance(
    R: pd.DataFrame, Rb: pd.DataFrame, period_lengths: (list[int] | None) = None
) -> pd.DataFrame:
    """Calculate table.ProbOutPerformance."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if period_lengths is None:
        period_lengths = [1, 3, 6, 9, 12, 18, 36]
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("table.ProbOutPerformance").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("Rb", xts_from_df(Rb)),
                    ("period_lengths", ro.vectors.IntVector(period_lengths)),
                ),
                lc,
            ),
            lc,
        )
