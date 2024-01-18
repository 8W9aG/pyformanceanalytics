"""The PerformanceAnalytics MarketTiming function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def MarketTiming(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    method: str,
    Rf: (pd.DataFrame | None) = None,
) -> pd.DataFrame:
    """Calculate MarketTiming."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
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
