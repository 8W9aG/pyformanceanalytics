"""The PerformanceAnalytics VolatilitySkewness function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.volatility_skewness import \
    VolatilitySkewness as RVolatilitySkewness
from .volatility_skewness_stat import VolatilitySkewnessStat


def VolatilitySkewness(
    R: pd.DataFrame,
    MAR: float = 0.0,
    stat: (str | VolatilitySkewnessStat | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate VolatilitySkewness."""
    if stat is None:
        stat = VolatilitySkewnessStat.VOLATILITY
    if backend == Backend.R:
        if isinstance(stat, VolatilitySkewnessStat):
            stat = stat.value
        return RVolatilitySkewness(R, stat, MAR=MAR)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for VolatilitySkewness"
    )
