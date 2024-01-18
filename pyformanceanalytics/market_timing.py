"""The PerformanceAnalytics MarketTiming function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.market_timing import MarketTiming as RMarketTiming
from .market_timing_method import MarketTimingMethod


def MarketTiming(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    method: (str | MarketTimingMethod | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate MarketTiming."""
    if method is None:
        method = MarketTimingMethod.TM
    if backend == Backend.R:
        if isinstance(method, MarketTimingMethod):
            method = method.value
        return RMarketTiming(Ra, Rb, method, Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for MarketTiming"
    )
