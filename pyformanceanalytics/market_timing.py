"""The PerformanceAnalytics MarketTiming function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def MarketTiming(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | None) = None,
    method: (str | None) = None,
) -> pd.DataFrame | float:
    """Calculate MarketTiming."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = "TM"
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("MarketTiming").rcall(  # type: ignore
                (
                    ("Ra", xts_from_df(Ra)),
                    ("Rb", xts_from_df(Rb)),
                    ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                    ("method", method),
                ),
                lc,
            ),
            lc,
        )
