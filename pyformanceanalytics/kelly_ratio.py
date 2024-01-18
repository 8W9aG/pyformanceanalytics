"""The PerformanceAnalytics KellyRatio function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def KellyRatio(
    R: pd.DataFrame, Rf: (pd.DataFrame | None) = None, method: (str | None) = None
) -> pd.DataFrame:
    """Calculate KellyRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = "half"
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("KellyRatio").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                    ("method", method),
                ),
                lc,
            ),
            lc,
        )
