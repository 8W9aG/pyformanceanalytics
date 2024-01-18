"""The PerformanceAnalytics MarketTiming function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.market_timing import MarketTiming as RMarketTiming


def MarketTiming(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | None) = None,
    method: (str | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate MarketTiming."""
    if backend == Backend.R:
        return RMarketTiming(Ra, Rb, Rf=Rf, method=method)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for MarketTiming"
    )
