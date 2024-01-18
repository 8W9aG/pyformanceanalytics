"""The PerformanceAnalytics SharpeRatio.modified function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def modified(
    R: pd.DataFrame,
    FUN: str,
    Rf: (pd.DataFrame | float),
    p: float = 0.95,
    weights: (pd.DataFrame | None) = None,
) -> pd.DataFrame:
    """Calculate SharpeRatio.modified."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("SharpeRatio.modified").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("Rf", xts_from_df(Rf) if isinstance(Rf, pd.DataFrame) else Rf),
                    ("p", p),
                    ("FUN", FUN),
                    ("weights", weights),
                ),
                lc,
            ),
            lc,
        )
