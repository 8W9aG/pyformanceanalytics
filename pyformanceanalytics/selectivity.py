"""The PerformanceAnalytics Selectivity function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.selectivity import Selectivity as RSelectivity


def Selectivity(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate Selectivity."""
    if backend == Backend.R:
        return RSelectivity(Ra, Rb, Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for Selectivity"
    )
