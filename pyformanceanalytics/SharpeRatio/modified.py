"""The PerformanceAnalytics SharpeRatio.modified function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.SharpeRatio.modified import modified as Rmodified
from .modified_function import ModifiedFunction


def modified(
    R: pd.DataFrame,
    Rf: (pd.DataFrame | None) = None,
    p: float = 0.95,
    FUN: (str | ModifiedFunction | None) = None,
    weights: (pd.DataFrame | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate SharpeRatio.modified."""
    if FUN is None:
        FUN = ModifiedFunction.STD_DEV
    if backend == Backend.R:
        if isinstance(FUN, ModifiedFunction):
            FUN = FUN.value
        return Rmodified(R, FUN, Rf=Rf, p=p, weights=weights)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for SharpeRatio.modified"
    )
