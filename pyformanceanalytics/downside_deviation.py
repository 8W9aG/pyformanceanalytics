"""The PerformanceAnalytics DownsideDeviation function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.downside_deviation import \
    DownsideDeviation as RDownsideDeviation


def DownsideDeviation(
    R: pd.DataFrame,
    MAR: float = 0.0,
    method: (str | None) = None,
    potential: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate DownsideDeviation."""
    if backend == Backend.R:
        return RDownsideDeviation(R, MAR=MAR, method=method, potential=potential)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for DownsideDeviation"
    )
