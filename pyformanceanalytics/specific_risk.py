"""The PerformanceAnalytics SpecificRisk function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.specific_risk import SpecificRisk as RSpecificRisk


def SpecificRisk(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate SpecificRisk."""
    if backend == Backend.R:
        return RSpecificRisk(Ra, Rb, Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for SpecificRisk"
    )
