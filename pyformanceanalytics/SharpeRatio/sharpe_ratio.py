"""The PerformanceAnalytics SharpeRatio function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.SharpeRatio.sharpe_ratio import SharpeRatio as RSharpeRatio
from .sharpe_ratio_function import SharpeRatioFunction


def SharpeRatio(
    R: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    p: float = 0.95,
    FUN: (str | SharpeRatioFunction | None) = None,
    weights: (pd.DataFrame | None) = None,
    annualize: bool = False,
    SE: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate SharpeRatio."""
    if FUN is None:
        FUN = SharpeRatioFunction.STD_DEV
    if backend == Backend.R:
        if isinstance(FUN, SharpeRatioFunction):
            FUN = FUN.value
        return RSharpeRatio(
            R, FUN, Rf, p=p, weights=weights, annualize=annualize, SE=SE
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for SharpeRatio"
    )
