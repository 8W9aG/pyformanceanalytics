"""The PerformanceAnalytics adjusted sharpe ratio function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R import adjusted_sharpe_ratio


def AdjustedSharpeRatio(
    R: pd.DataFrame, Rf: (pd.DataFrame | float) = 0.0, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate AdjustedSharpeRatio."""
    if backend == Backend.R:
        return adjusted_sharpe_ratio.AdjustedSharpeRatio(R, Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for AdjustedSharpeRatio"
    )
