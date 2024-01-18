"""The PerformanceAnalytics DownsideDeviation function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.downside_deviation import \
    DownsideDeviation as RDownsideDeviation
from .downside_deviation_method import DownsideDeviationMethod


def DownsideDeviation(
    R: pd.DataFrame,
    MAR: float = 0.0,
    method: (str | DownsideDeviationMethod | None) = None,
    potential: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate DownsideDeviation."""
    if method is None:
        method = DownsideDeviationMethod.FULL
    if backend == Backend.R:
        if isinstance(method, DownsideDeviationMethod):
            method = method.value
        return RDownsideDeviation(R, method, MAR=MAR, potential=potential)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for DownsideDeviation"
    )
