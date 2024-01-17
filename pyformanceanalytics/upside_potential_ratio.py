"""The PerformanceAnalytics UpsidePotentialRatio function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def UpsidePotentialRatio(
    R: pd.DataFrame, MAR: float = 0.0, method: (str | None) = None
) -> pd.DataFrame | float:
    """Calculate UpsidePotentialRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = "subset"
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("UpsidePotentialRatio").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("MAR", MAR),
                    ("method", method),
                ),
                lc,
            ),
            lc,
        )
