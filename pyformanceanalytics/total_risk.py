"""The PerformanceAnalytics TotalRisk function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.total_risk import TotalRisk as RTotalRisk


def TotalRisk(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate TotalRisk."""
    if backend == Backend.R:
        return RTotalRisk(Ra, Rb, Rf=Rf)
    raise NotImplementedError(f"Backend {backend.value} not implemented for TotalRisk")
