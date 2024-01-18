"""The PerformanceAnalytics centeredmoment function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def centeredmoment(R: pd.DataFrame, power: float = 2.0) -> pd.DataFrame:
    """Calculate centeredmoment."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("centeredmoment").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("power", power),
                ),
                lc,
            ),
            lc,
        )
