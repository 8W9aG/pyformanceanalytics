"""The PerformanceAnalytics SharpeRatio function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df
from .sharpe_ratio_function import SharpeRatioFunction


def SharpeRatio(
    R: pd.DataFrame,
    Rf: (pd.DataFrame | None) = None,
    p: float = 0.95,
    FUN: (str | SharpeRatioFunction | None) = None,
    weights: (pd.DataFrame | None) = None,
    annualize: bool = False,
    SE: bool = False,
) -> pd.DataFrame:
    """Calculate SharpeRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if FUN is None:
        FUN = SharpeRatioFunction.STD_DEV
    if isinstance(FUN, SharpeRatioFunction):
        FUN = FUN.value
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("SharpeRatio").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                    ("p", p),
                    ("FUN", FUN),
                    ("weights", weights),
                    ("annualize", annualize),
                    ("SE", SE),
                ),
                lc,
            ),
            lc,
        )
