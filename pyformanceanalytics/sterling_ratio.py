"""The PerformanceAnalytics sterling ratio function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def SterlingRatio(R: pd.DataFrame, excess: float = 0.1) -> pd.DataFrame:
    """Calculate SterlingRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("SterlingRatio").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("excess", excess),
                ),
                lc,
            ),
            lc,
        )
