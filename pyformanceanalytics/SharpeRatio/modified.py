"""The PerformanceAnalytics SharpeRatio.modified function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame_or_float
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df
from .modified_function import ModifiedFunction


def modified(
    R: pd.DataFrame,
    Rf: (pd.DataFrame | None) = None,
    p: float = 0.95,
    FUN: (str | ModifiedFunction | None) = None,
    weights: (pd.DataFrame | None) = None,
) -> pd.DataFrame | float:
    """Calculate SharpeRatio.modified."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if FUN is None:
        FUN = ModifiedFunction.STD_DEV
    if isinstance(FUN, ModifiedFunction):
        FUN = FUN.value
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("SharpeRatio.modified").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                    ("p", p),
                    ("FUN", FUN),
                    ("weights", weights),
                ),
                lc,
            ),
            lc,
        )
