"""The PerformanceAnalytics table.SpecificRisk function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.specific_risk import SpecificRisk as RSpecificRisk


def SpecificRisk(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    digits: int = 4,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate table.SpecificRisk."""
    if backend == Backend.R:
        return RSpecificRisk(Ra, Rb, Rf, digits=digits)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.SpecificRisk"
    )
