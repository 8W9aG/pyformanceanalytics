"""The PerformanceAnalytics SharpeRatio.annualized function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.SharpeRatio.annualized import annualized as Rannualized


def annualized(
    R: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    geometric: bool = True,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate SharpeRatio.annualized."""
    if backend == Backend.R:
        return Rannualized(R, Rf, geometric=geometric)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for SharpeRatio.annualized"
    )
