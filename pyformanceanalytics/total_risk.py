"""The PerformanceAnalytics TotalRisk function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.total_risk import TotalRisk as RTotalRisk


def TotalRisk(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate TotalRisk."""
    if backend == Backend.R:
        return RTotalRisk(Ra, Rb, Rf)
    raise NotImplementedError(f"Backend {backend.value} not implemented for TotalRisk")
