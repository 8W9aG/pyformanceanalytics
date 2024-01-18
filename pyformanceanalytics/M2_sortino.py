"""The PerformanceAnalytics M2Sortino function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.M2_sortino import M2Sortino as RM2Sortino


def M2Sortino(
    Ra: pd.DataFrame, Rb: pd.DataFrame, MAR: float, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate M2Sortino."""
    if backend == Backend.R:
        return RM2Sortino(Ra, Rb, MAR)
    raise NotImplementedError(f"Backend {backend.value} not implemented for M2Sortino")
