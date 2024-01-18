"""The PerformanceAnalytics kurtosis function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def kurtosis(
    x: pd.DataFrame,
    method: str,
    na_rm: bool = False,
) -> pd.DataFrame | float:
    """Calculate kurtosis."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("kurtosis").rcall(  # type: ignore
                (
                    ("x", xts_from_df(x)),
                    ("na.rm", na_rm),
                    ("method", method),
                ),
                lc,
            ),
            lc,
        )
