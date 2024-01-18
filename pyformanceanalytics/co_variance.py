"""The PerformanceAnalytics CoVariance function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.co_variance import CoVariance as RCoVariance


def CoVariance(
    Ra: pd.DataFrame, Rb: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate CoVariance."""
    if backend == Backend.R:
        return RCoVariance(Ra, Rb)
    raise NotImplementedError(f"Backend {backend.value} not implemented for CoVariance")
