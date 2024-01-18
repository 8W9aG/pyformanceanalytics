"""The PerformanceAnalytics MSquaredExcess function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.m_squared_excess import MSquaredExcess as RMSquaredExcess


def MSquaredExcess(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | None) = None,
    method: (str | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate MSquaredExcess."""
    if backend == Backend.R:
        return RMSquaredExcess(Ra, Rb, Rf=Rf, method=method)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for MSquaredExcess"
    )
