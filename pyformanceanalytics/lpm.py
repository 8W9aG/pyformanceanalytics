"""The PerformanceAnalytics lpm function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def lpm(
    R: pd.DataFrame,
    n: int = 2,
    threshold: int = 0,
    about_mean: bool = False,
    SE: bool = False,
) -> pd.DataFrame | float:
    """Calculate lpm."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("lpm").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("n", n),
                    ("threshold", threshold),
                    ("about.mean", about_mean),
                    ("SE", SE),
                ),
                lc,
            ),
            lc,
        )
