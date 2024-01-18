"""The PerformanceAnalytics NetSelectivity function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.net_selectivity import NetSelectivity as RNetSelectivity


def NetSelectivity(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate NetSelectivity."""
    if backend == Backend.R:
        return RNetSelectivity(Ra, Rb, Rf)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for NetSelectivity"
    )
