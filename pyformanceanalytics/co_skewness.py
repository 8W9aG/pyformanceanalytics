"""The PerformanceAnalytics CoSkewness function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.co_skewness import CoSkewness as RCoSkewness


def CoSkewness(
    Ra: pd.DataFrame, Rb: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate CoSkewness."""
    if backend == Backend.R:
        return RCoSkewness(Ra, Rb)
    raise NotImplementedError(f"Backend {backend.value} not implemented for CoSkewness")
