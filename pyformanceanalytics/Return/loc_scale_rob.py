"""The PerformanceAnalytics Return.locScaleRob function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame_or_float
from ..rimports import (PERFORMANCE_ANALYTICS_PACKAGE, PKG_PACKAGE,
                        ensure_packages_present)
from ..xts import xts_from_df


def locScaleRob(
    R: pd.DataFrame, alpha_robust: float = 0.05, normal_efficiency: float = 0.99
) -> pd.DataFrame | float:
    """Calculate Return.locScaleRob."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE, PKG_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("Return.locScaleRob").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("alpha.robust", alpha_robust),
                    ("normal.efficiency", normal_efficiency),
                ),
                lc,
            ),
            lc,
        )
