"""The PerformanceAnalytics CoKurtosis function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.co_kurtosis import CoKurtosis as RCoKurtosis


def CoKurtosis(
    Ra: pd.DataFrame, Rb: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame | float:
    """Calculate CoKurtosis."""
    if backend == Backend.R:
        return RCoKurtosis(Ra, Rb)
    raise NotImplementedError(f"Backend {backend.value} not implemented for CoKurtosis")
