"""The PerformanceAnalytics SmoothingIndex function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def SmoothingIndex(
    R: pd.DataFrame, neg_thetas: bool = False, ma_order: int = 2, verbose: bool = False
) -> pd.DataFrame:
    """Calculate SmoothingIndex."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("SmoothingIndex").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("neg.thetas", neg_thetas),
                    ("MAorder", ma_order),
                    ("verbose", verbose),
                ),
                lc,
            ),
            lc,
        )
