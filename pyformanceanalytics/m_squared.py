"""The PerformanceAnalytics MSquared function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.m_squared import MSquared as RMSquared


def MSquared(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate MSquared."""
    if backend == Backend.R:
        return RMSquared(Ra, Rb, Rf)
    raise NotImplementedError(f"Backend {backend.value} not implemented for MSquared")
