"""The PerformanceAnalytics VolatilitySkewness function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.volatility_skewness import \
    VolatilitySkewness as RVolatilitySkewness


def VolatilitySkewness(
    R: pd.DataFrame,
    MAR: float = 0.0,
    stat: (str | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate VolatilitySkewness."""
    if backend == Backend.R:
        return RVolatilitySkewness(R, MAR=MAR, stat=stat)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for VolatilitySkewness"
    )
